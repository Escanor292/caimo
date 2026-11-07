# Supervised & Fine-Tuned AI Text Detectors

Supervised detectors formulate AI text detection as a binary classification problem ($y \in \{0, 1\}$: 0 = Human, 1 = AI). They fine-tune transformer encoders (RoBERTa, DeBERTa, ModernBERT) or decoder LLMs on curated paired datasets.

---

## 1. AI Detector From Scratch (FastAPI + React UI)

* **Repository:** [rasbt/ai-detector-from-scratch](https://github.com/rasbt/ai-detector-from-scratch)
* **Author:** Sebastian Raschka (Author of *Build a Large Language Model (From Scratch)*)
* **Architecture:**
  * End-to-end framework to fine-tune state-of-the-art lightweight encoders:
    * **ModernBERT** (fast 8192 context window, FlashAttention-2 support)
    * **DistilBERT** (ultra-fast, CPU friendly)
    * **Qwen 2.5** / **Llama-3** (encoder head or LoRA classification head)
  * Pre-packaged with:
    * Clean training loops with mixed precision (`bfloat16`).
    * Production-ready **FastAPI** backend for REST inference.
    * Modern **React + Tailwind** frontend UI showing detection confidence meters.

---

## 2. Desklib AI Text Detector (DeBERTa-v3)

* **Repository:** [desklib/ai-text-detector](https://github.com/desklib/ai-text-detector)
* **Hugging Face Model:** `desklib/ai-text-detector` (or related checkpoints)
* **Architecture:** DeBERTa-v3-base/large fine-tuned on academic writing, student essays, and multi-LLM outputs (ChatGPT, GPT-4, Claude 3, Gemini, LLaMA-3).
* **Strength:** DeBERTa-v3 uses disentangled attention (separate vectors for content and relative position), yielding substantially higher sensitivity on long essays and subtle structural AI cadence than vanilla BERT.
* **Inference Code:**
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "desklib/ai-text-detector"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def predict_ai(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=-1)[0]
    return {
        "Human_Score": probs[0].item(),
        "AI_Score": probs[1].item(),
        "Is_AI": probs[1].item() > 0.5
    }
```

---

## 3. OpenAI GPT-2 Output Dataset & RoBERTa Detector

* **Repository:** [openai/gpt-2-output-dataset](https://github.com/openai/gpt-2-output-dataset)
* **Hugging Face Models:** `roberta-base-openai-detector`, `roberta-large-openai-detector`
* **Strength:** Historical industry baseline trained directly by OpenAI on WebText vs GPT-2 1.5B generations.
* **Limitations:** Prone to false negatives against modern frontier LLMs (GPT-4o, Claude 3.5, Gemini 1.5) due to distribution shift. Serves as a fast, lightweight baseline.

---

## 4. Fine-Tuning Recipes for Vietnamese (Đặc thù tiếng Việt)

Standard English detectors often perform poorly on Vietnamese text due to subword fragmentation (e.g. standard BPE splitting Vietnamese diacritics into multiple disjoint byte tokens).

### Recommended Pretrained Backbones for Vietnamese:
1. **VinAI PhoBERT (`vinai/phobert-base-v2`, `vinai/phobert-large`):**
   * Pre-trained specifically on 20GB of Vietnamese text using syllable/word segmentation.
   * High performance when fine-tuned on human Vietnamese articles (VNExpress, TuoiTre, Wikipedia) vs translated/generated texts from GPT-4o / Claude.
2. **XLM-RoBERTa (`xlm-roberta-base`, `xlm-roberta-large`):**
   * Multilingual cross-lingual transfer. Can be trained jointly on English + Vietnamese pairs.
3. **Vietnamese Text Preprocessing:**
   * Apply word segmentation via `pyvi` or `rdrsegmenter` before tokenization if using `PhoBERT`.
