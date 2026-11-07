#!/usr/bin/env python3
"""
Lightweight offline statistical analyzer for text.
Computes linguistic signatures commonly differing between human writing and AI:
- Perplexity proxy (Shannon Entropy of unigrams)
- Burstiness (Sentence length variation)
- Type-Token Ratio (Vocabulary richness / diversity)
- Repetition & n-gram frequency distribution
Language-agnostic: Works for Vietnamese, English, and other languages.
"""

import sys
import math
import re
from collections import Counter

def analyze_text_statistics(text: str):
    # Split sentences (handles . ! ? and newlines)
    sentences = [s.strip() for s in re.split(r'[.!?\n]+', text) if len(s.strip()) > 3]
    
    # Tokenize words (lowercase alphanumeric + Unicode letters for Vietnamese diacritics)
    words = re.findall(r'\b[^\W\d_]+\b', text.lower())
    
    total_words = len(words)
    unique_words = len(set(words))
    
    if total_words == 0:
        return {"error": "Text has no words to analyze."}
        
    # 1. Type-Token Ratio (TTR)
    ttr = unique_words / total_words
    
    # 2. Shannon Entropy of Unigrams
    counts = Counter(words)
    entropy = -sum((c / total_words) * math.log2(c / total_words) for c in counts.values())
    
    # 3. Burstiness (Coefficient of Variation of Sentence Lengths)
    sentence_lengths = [len(s.split()) for s in sentences] if sentences else [total_words]
    mean_len = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    if len(sentence_lengths) > 1 and mean_len > 0:
        variance = sum((l - mean_len) ** 2 for l in sentence_lengths) / (len(sentence_lengths) - 1)
        std_len = math.sqrt(variance)
        burstiness = std_len / mean_len # Coefficient of variation
    else:
        burstiness = 0.0

    # 4. Repetition rate (top 5 words proportion)
    top5_sum = sum(c for _, c in counts.most_common(5))
    top5_ratio = top5_sum / total_words if total_words > 0 else 0

    # 5. Heuristic AI Probability Indicator
    # AI text typically has:
    # - Lower burstiness (more uniform sentence lengths)
    # - Moderate to high entropy with very predictable transitions
    # - Highly regular paragraph structure
    ai_indicators = []
    if burstiness < 0.35 and len(sentences) >= 3:
        ai_indicators.append("Low burstiness: Sentence lengths are unusually uniform (typical of AI).")
    if ttr < 0.40 and total_words > 100:
        ai_indicators.append("Low vocabulary diversity (TTR < 0.40).")
    if top5_ratio > 0.25:
        ai_indicators.append("High top-word concentration.")

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "num_sentences": len(sentences),
        "mean_sentence_length": round(mean_len, 2),
        "type_token_ratio_ttr": round(ttr, 4),
        "shannon_entropy": round(entropy, 4),
        "burstiness_index": round(burstiness, 4),
        "top5_frequent_words": counts.most_common(5),
        "heuristic_observations": ai_indicators or ["Natural sentence variation detected (typical of human text)."]
    }

def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        print("Usage: python text_stats.py 'Đoạn văn bản cần phân tích...'")
        sys.exit(1)
        
    stats = analyze_text_statistics(text)
    print("=" * 60)
    print("Linguistic Signature & Statistical Text Analysis")
    print("=" * 60)
    for k, v in stats.items():
        print(f"{k:<25}: {v}")
    print("=" * 60)

if __name__ == "__main__":
    main()
