# Web & API Integration Guide (Zero-GPU & Serverless)

How to integrate AI text detection into modern web applications (Next.js, React, FastAPI, Node.js) without maintaining expensive dedicated GPU infrastructure.

---

## Architecture Comparison

| Approach | Latency | Infrastructure Cost | Privacy | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Hugging Face Inference API** | ~200–500 ms | Free tier / Pay-per-token | Texts sent to HF servers | Quick prototypes, MVP, SaaS |
| **Transformers.js (In-Browser)** | ~500–1500 ms | **$0.00 (Runs on user's device)** | 100% private (never leaves browser) | Chrome extensions, privacy-first apps |
| **FastAPI Microservice (Self-hosted)** | ~50–150 ms | VM/Server cost (CPU or GPU) | Private within your VPC | Enterprise production, high volume |

---

## 1. Hugging Face Inference API (Next.js / Node.js)

Call pre-trained detector models directly via Hugging Face's serverless endpoints without downloading weights or managing PyTorch environments.

### Example in Next.js Route Handler (`app/api/detect/route.ts`):

```typescript
import { NextResponse } from 'next/server';

const HF_API_KEY = process.env.HF_API_KEY;
// Recommended models:
// 1. "desklib/ai-text-detector" (DeBERTa-v3 based, strong on modern LLMs)
// 2. "roberta-base-openai-detector" (Fast baseline)
const MODEL_ID = 'desklib/ai-text-detector';

export async function POST(req: Request) {
  try {
    const { text } = await req.json();

    if (!text || text.length < 50) {
      return NextResponse.json(
        { error: 'Text must be at least 50 characters long for reliable detection.' },
        { status: 400 }
      );
    }

    const response = await fetch(
      `https://api-inference.huggingface.co/models/${MODEL_ID}`,
      {
        headers: {
          Authorization: `Bearer ${HF_API_KEY}`,
          'Content-Type': 'application/json',
        },
        method: 'POST',
        body: JSON.stringify({ inputs: text }),
      }
    );

    if (!response.ok) {
      const err = await response.text();
      return NextResponse.json({ error: `HF API error: ${err}` }, { status: response.status });
    }

    const result = await response.json();
    // Result format: [[ { label: "Human", score: 0.12 }, { label: "AI", score: 0.88 } ]]
    return NextResponse.json({ success: true, result });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

---

## 2. In-Browser Detection via Transformers.js (Zero Server Cost)

Using `@xenova/transformers`, you can run a quantized ONNX AI detector directly inside the user's browser via WebAssembly/WebGPU.

### Installation:
```bash
npm install @xenova/transformers
```

### React / Next.js Component Hook:
```javascript
import { useEffect, useState, useRef } from 'react';
import { pipeline } from '@xenova/transformers';

export function useAIDetector() {
  const [loading, setLoading] = useState(true);
  const classifier = useRef(null);

  useEffect(() => {
    async function loadModel() {
      // Loads quantized ONNX model directly in browser
      classifier.current = await pipeline(
        'text-classification',
        'Xenova/roberta-base-openai-detector'
      );
      setLoading(false);
    }
    loadModel();
  }, []);

  const detect = async (text) => {
    if (!classifier.current) return null;
    const output = await classifier.current(text);
    return output; // [{ label: "Real", score: 0.15 }] or [{ label: "Fake", score: 0.85 }]
  };

  return { detect, loading };
}
```

---

## 3. Production FastAPI Microservice (Python)

See [`scripts/serve_fastapi.py`](../scripts/serve_fastapi.py) for the ready-to-run implementation with CORS, token batching, and confidence thresholding.
