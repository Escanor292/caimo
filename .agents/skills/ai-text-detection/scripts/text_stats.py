#!/usr/bin/env python3
"""
Academic Humanizer & Text Signature Auditor.
Computes linguistic signatures to assess AI detection risk (Turnitin, GPTZero, Desklib):
- Burstiness Index (Sentence length variation) [Target: > 0.45]
- Type-Token Ratio (Vocabulary diversity) [Target: > 0.45]
- Shannon Entropy
- Red-Flag Cliché Detection (Both Vietnamese and English)
"""

import sys
import math
import re
from collections import Counter

# Banned AI red-flag patterns
BANNED_VIETNAMESE = [
    r"trong bối cảnh",
    r"không thể phủ nhận",
    r"đóng vai trò (vô cùng )?(quan trọng|then chốt|không thể thiếu)",
    r"như chúng ta đã biết",
    r"tóm lại, việc",
    r"là một bước tiến mang tính đột phá",
    r"kỷ nguyên số (4\.0)?",
    r"không chỉ.*?mà còn.*?",
]

BANNED_ENGLISH = [
    r"\bdelve(\b|s|d|ing)",
    r"\btapestry\b",
    r"\btestament\b",
    r"\bunderscore(s|d)?\b",
    r"\bpivotal\b",
    r"\bintricate\b",
    r"\bcrucial\b",
    r"\bfoster(s|ed|ing)?\b",
    r"\bharness(es|ed|ing)?\b",
    r"\bembark(s|ed|ing)?\b",
    r"\bbeacon\b",
    r"\brealm(s)?\b",
    r"\bparamount\b",
    r"\bmoreover\b",
    r"\bfurthermore\b",
    r"in today's (fast-paced|digital|modern) world",
    r"it is (worth noting|important to remember)",
    r"a double-edged sword"
]

def audit_text(text: str):
    # Split sentences
    sentences = [s.strip() for s in re.split(r'[.!?\n]+', text) if len(s.strip()) > 3]
    words = re.findall(r'\b[^\W\d_]+\b', text.lower())
    total_words = len(words)
    unique_words = len(set(words))

    if total_words == 0:
        return {"error": "Text has no words to analyze."}

    # 1. Type-Token Ratio (TTR)
    ttr = unique_words / total_words

    # 2. Shannon Entropy
    counts = Counter(words)
    entropy = -sum((c / total_words) * math.log2(c / total_words) for c in counts.values())

    # 3. Burstiness (Coefficient of variation of sentence lengths)
    sentence_lengths = [len(s.split()) for s in sentences] if sentences else [total_words]
    mean_len = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    if len(sentence_lengths) > 1 and mean_len > 0:
        variance = sum((l - mean_len) ** 2 for l in sentence_lengths) / (len(sentence_lengths) - 1)
        std_len = math.sqrt(variance)
        burstiness = std_len / mean_len
    else:
        burstiness = 0.0

    # 4. Check Red-Flag Clichés
    detected_cliches = []
    text_lower = text.lower()
    for pat in BANNED_VIETNAMESE:
        matches = re.findall(pat, text_lower)
        if matches:
            detected_cliches.append(f"[VI Red Flag] '{pat}' ({len(matches)} match)")
    for pat in BANNED_ENGLISH:
        matches = re.findall(pat, text_lower)
        if matches:
            detected_cliches.append(f"[EN Red Flag] '{pat}' ({len(matches)} match)")

    # 5. Overall Humanization Assessment
    pass_burstiness = burstiness >= 0.42
    pass_ttr = ttr >= 0.42 or total_words < 50
    pass_cliches = len(detected_cliches) == 0

    if pass_burstiness and pass_ttr and pass_cliches:
        status = "PASSED - High Human Stance (Safe against Turnitin / GPTZero)"
    elif not pass_cliches:
        status = "FAILED - Contains banned AI clichés (Immediate Flag)"
    elif not pass_burstiness:
        status = "WARNING - Low Burstiness (Sentences are too uniform; needs rhythm variation)"
    else:
        status = "WARNING - Low vocabulary diversity"

    return {
        "status": status,
        "total_words": total_words,
        "num_sentences": len(sentences),
        "mean_sentence_length": round(mean_len, 2),
        "burstiness_index": round(burstiness, 4),
        "target_burstiness": ">= 0.45",
        "type_token_ratio_ttr": round(ttr, 4),
        "shannon_entropy": round(entropy, 4),
        "detected_cliches": detected_cliches or ["None detected (Clean)"],
        "sentence_length_distribution": sentence_lengths[:15]
    }

def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        print("Usage: python text_stats.py 'Đoạn văn bản cần kiểm tra...'")
        sys.exit(1)

    res = audit_text(text)
    print("=" * 65)
    print("ACADEMIC HUMANIZER AUDIT REPORT")
    print("=" * 65)
    for k, v in res.items():
        if k == "detected_cliches" and isinstance(v, list):
            print(f"{k:<25}:")
            for c in v:
                print(f"   -> {c}")
        else:
            print(f"{k:<25}: {v}")
    print("=" * 65)

if __name__ == "__main__":
    main()
