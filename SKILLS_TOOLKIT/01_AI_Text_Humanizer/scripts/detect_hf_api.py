#!/usr/bin/env python3
"""
CLI tool for AI Text Detection using Hugging Face Inference API.
Supports English models (desklib, openai-roberta) and multilingual/Vietnamese models.
"""

import sys
import os
import json
import argparse
import urllib.request
import urllib.error

DEFAULT_MODEL = "desklib/ai-text-detector"

def query_hf_api(text: str, model_id: str, api_token: str = None):
    url = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Content-Type": "application/json"}
    if api_token:
        headers["Authorization"] = f"Bearer {api_token}"
    
    payload = json.dumps({"inputs": text}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        return {"error": f"HTTP {e.code}: {err_msg}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Detect AI-generated text via Hugging Face API.")
    parser.add_argument("text", nargs="?", help="Text to analyze (or read from stdin).")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"HF Model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("--token", default=os.environ.get("HF_TOKEN") or os.environ.get("HF_API_KEY"), help="HF API Token")
    args = parser.parse_args()

    content = args.text
    if not content:
        if not sys.stdin.isatty():
            content = sys.stdin.read().strip()
        else:
            print("Usage: python detect_hf_api.py 'Your text to inspect...' [--model MODEL]")
            sys.exit(1)

    if len(content) < 30:
        print("Warning: Text is very short (< 30 characters). AI detectors are unreliable on short phrases.")

    print(f"[*] Querying model: {args.model}")
    print(f"[*] Text length: {len(content)} chars (~{len(content.split())} words)")
    result = query_hf_api(content, args.model, args.token)
    print("\n[+] Detection Result:")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
