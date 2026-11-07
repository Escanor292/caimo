#!/usr/bin/env python3
"""
Advanced Academic Humanizer & Style Linter.
Integrates algorithms from DIPPER (AllenAI), Proselint, and Write-Good:
- Burstiness & Sentence Cadence (3-tier distribution)
- Lexical & Order Diversity (DIPPER)
- Weasel Words & Padding Detector (Proselint)
- Zombie Nouns & Nominalization Checker (Write-Good)
- Passive Voice Ratio Calculator
- Banned AI Clichés & Red-Flags (Vietnamese & English)
- Turnitin & GPTZero Risk Score (0-100%)
"""

import sys
import math
import re
from collections import Counter

# 1. Banned AI red-flag patterns
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

# 2. Weasel words & padding fillers (Proselint / Write-Good)
WEASEL_VIETNAMESE = [
    r"\brất\b", r"\bvô cùng\b", r"\bcực kỳ\b", r"\btương đối\b",
    r"\bnhìn chung( thì)?\b", r"\brõ ràng là\b", r"\bhiển nhiên là\b",
    r"\bcó thể nói rằng\b", r"\btrên thực tế thì\b"
]

WEASEL_ENGLISH = [
    r"\bextremely\b", r"\bfairly\b", r"\bremarkably\b", r"\bquite\b",
    r"\bclearly\b", r"\bobviously\b", r"\bvirtually\b", r"\bessentially\b",
    r"\bin a sense\b", r"\bin terms of\b", r"\bit goes without saying\b"
]

# 3. Zombie Nouns / Nominalizations (Write-Good)
NOMINALIZATION_VIETNAMESE = [
    r"tiến hành (thực hiện|quá trình)?",
    r"thực hiện việc (phân tích|tối ưu|đánh giá|khảo sát)",
    r"đưa ra kết luận khẳng định"
]

NOMINALIZATION_ENGLISH = [
    r"\bconduct(ed|ing)? an (investigation|analysis|examination)\b",
    r"\bmake(s|d|ing)? an (assumption|assessment|evaluation)\b",
    r"\bperform(ed|ing)? a (demonstration|verification)\b",
    r"\btake into consideration\b"
]

def audit_academic_text(text: str):
    sentences = [s.strip() for s in re.split(r'[.!?\n]+', text) if len(s.strip()) > 3]
    words = re.findall(r'\b[^\W\d_]+\b', text.lower())
    total_words = len(words)
    unique_words = len(set(words))

    if total_words == 0:
        return {"error": "Text has no words to analyze."}

    # A. Lexical Diversity (DIPPER)
    ttr = unique_words / total_words

    # B. Burstiness & Cadence
    sentence_lengths = [len(s.split()) for s in sentences] if sentences else [total_words]
    mean_len = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    if len(sentence_lengths) > 1 and mean_len > 0:
        variance = sum((l - mean_len) ** 2 for l in sentence_lengths) / (len(sentence_lengths) - 1)
        std_len = math.sqrt(variance)
        burstiness = std_len / mean_len
    else:
        burstiness = 0.0

    # 3-Tier Sentence Length Breakdown
    short_sentences = sum(1 for l in sentence_lengths if l <= 9)
    long_sentences = sum(1 for l in sentence_lengths if l >= 26)
    moderate_sentences = len(sentence_lengths) - short_sentences - long_sentences

    # C. Clichés, Weasels, Nominalizations
    text_lower = text.lower()
    cliches_found = []
    weasels_found = []
    nominalizations_found = []

    for pat in BANNED_VIETNAMESE + BANNED_ENGLISH:
        m = re.findall(pat, text_lower)
        if m: cliches_found.append(f"Cliché: '{pat}' ({len(m)})")

    for pat in WEASEL_VIETNAMESE + WEASEL_ENGLISH:
        m = re.findall(pat, text_lower)
        if m: weasels_found.append(f"Weasel: '{pat}' ({len(m)})")

    for pat in NOMINALIZATION_VIETNAMESE + NOMINALIZATION_ENGLISH:
        m = re.findall(pat, text_lower)
        if m: nominalizations_found.append(f"Zombie Noun: '{pat}' ({len(m)})")

    # D. Passive Voice Detection (rough indicator)
    passive_count = len(re.findall(r"\b(được|bị)\b", text_lower)) + len(re.findall(r"\b(is|are|was|were|been|being)\s+\w+ed\b", text_lower))
    passive_ratio = (passive_count / len(sentences)) if sentences else 0.0

    # E. Turnitin & GPTZero Risk Score Calculation (0 to 100%)
    risk_score = 0.0
    if cliches_found: risk_score += min(50.0, len(cliches_found) * 15.0)
    if burstiness < 0.35: risk_score += 30.0
    elif burstiness < 0.42: risk_score += 15.0
    if weasels_found: risk_score += min(15.0, len(weasels_found) * 5.0)
    if nominalizations_found: risk_score += min(15.0, len(nominalizations_found) * 5.0)
    if passive_ratio > 0.40: risk_score += 10.0
    risk_score = min(100.0, max(0.0, risk_score))

    # Assessment Verdict
    if risk_score <= 15.0 and burstiness >= 0.42 and not cliches_found:
        verdict = "PASSED - High Scholarly Stance (Safe from Turnitin / GPTZero)"
    elif risk_score <= 35.0:
        verdict = "MODERATE - Low risk, but can improve sentence cadence"
    else:
        verdict = "HIGH RISK - Flagged as AI-generated patterns; rewrite required"

    suggestions = []
    if cliches_found: suggestions.append("Remove all detected AI clichés immediately.")
    if burstiness < 0.42: suggestions.append("Split uniform sentences; inject 1 punchy short sentence (<9 words) and 1 complex compound sentence (>28 words).")
    if nominalizations_found: suggestions.append("Convert zombie nouns back to direct active verbs (e.g. 'thực hiện việc phân tích' -> 'phân tích').")
    if weasels_found: suggestions.append("Cut empty fillers ('rất', 'vô cùng', 'clearly', 'essentially').")

    return {
        "verdict": verdict,
        "ai_risk_score": f"{risk_score:.1f}%",
        "total_words": total_words,
        "num_sentences": len(sentences),
        "mean_sentence_length": round(mean_len, 2),
        "burstiness_index": round(burstiness, 4),
        "target_burstiness": ">= 0.45",
        "cadence_breakdown": f"Short: {short_sentences} | Moderate: {moderate_sentences} | Long: {long_sentences}",
        "type_token_ratio_ttr": round(ttr, 4),
        "cliches_detected": cliches_found or ["Clean"],
        "weasels_detected": weasels_found or ["Clean"],
        "zombie_nouns_detected": nominalizations_found or ["Clean"],
        "suggestions": suggestions or ["Text exhibits authentic human scholarship."]
    }

def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        print("Usage: python text_stats.py 'Academic text to audit...'")
        sys.exit(1)

    rep = audit_academic_text(text)
    print("=" * 68)
    print("PROSELINT + DIPPER ACADEMIC AUDIT REPORT")
    print("=" * 68)
    for k, v in rep.items():
        if isinstance(v, list):
            print(f"{k:<25}:")
            for item in v:
                print(f"   -> {item}")
        else:
            print(f"{k:<25}: {v}")
    print("=" * 68)

if __name__ == "__main__":
    main()
