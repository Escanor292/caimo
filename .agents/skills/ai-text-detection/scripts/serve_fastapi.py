#!/usr/bin/env python3
"""
Production-ready FastAPI microservice boilerplate for AI text detection.
Can be deployed via Docker, AWS ECS, GCP Cloud Run, or Railway.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
import os

app = FastAPI(
    title="AI Text Detection Microservice",
    description="REST API for detecting AI-generated text using transformer models.",
    version="1.0.0"
)

class DetectionRequest(BaseModel):
    text: str = Field(..., min_length=20, max_length=10000, description="The text content to analyze.")
    model_name: Optional[str] = Field("desklib/ai-text-detector", description="Hugging Face model ID")

class DetectionResponse(BaseModel):
    text_length: int
    word_count: int
    ai_score: float
    human_score: float
    verdict: str
    confidence: str

# Lazy-loaded model holder
model_cache = {}

def get_classifier(model_name: str):
    if model_name not in model_cache:
        try:
            from transformers import pipeline
            model_cache[model_name] = pipeline("text-classification", model=model_name, device=-1)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to load model {model_name}: {str(e)}")
    return model_cache[model_name]

@app.get("/")
def health_check():
    return {"status": "ok", "service": "ai-text-detector"}

@app.post("/detect", response_model=DetectionResponse)
def detect_ai_text(req: DetectionRequest):
    words = req.text.split()
    if len(words) < 10:
        raise HTTPException(status_code=400, detail="Text must contain at least 10 words for meaningful detection.")

    # Option A: In-memory pipeline
    classifier = get_classifier(req.model_name)
    results = classifier(req.text[:2000]) # Truncate to safe context length
    
    # Parse labels (e.g. LABEL_0 / LABEL_1 or Fake / Real)
    top_result = results[0]
    score = top_result['score']
    label = top_result['label'].upper()

    is_ai = "FAKE" in label or "AI" in label or "LABEL_1" in label
    ai_prob = score if is_ai else (1.0 - score)
    human_prob = 1.0 - ai_prob

    verdict = "AI-Generated" if ai_prob > 0.5 else "Human-Written"
    confidence = "High" if max(ai_prob, human_prob) > 0.85 else "Moderate"

    return DetectionResponse(
        text_length=len(req.text),
        word_count=len(words),
        ai_score=round(ai_prob, 4),
        human_score=round(human_prob, 4),
        verdict=verdict,
        confidence=confidence
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
