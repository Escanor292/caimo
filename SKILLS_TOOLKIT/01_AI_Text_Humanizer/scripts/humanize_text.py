#!/usr/bin/env python3
"""
Automated Academic Text Humanizer & Rewriter Helper.
Applies mechanical transformations derived from DIPPER, Proselint, and Write-Good:
1. Strips padding weasel words (clearly, obviously, rất, vô cùng...)
2. De-nominalizes zombie nouns (conduct an analysis -> analyze, thực hiện việc tối ưu -> tối ưu)
3. Strips AI cliché throat-clearing openers and praise phrases
4. Outputs side-by-side comparison with audit scores before & after.
"""

import sys
import re
import os

# Import our audit engine from text_stats
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from text_stats import audit_academic_text

# Substitution dictionaries for nominalizations, weasels, and clichés
REPLACEMENTS_VIETNAMESE = [
    # Zombie nouns -> active verbs
    (r"\btiến hành thực hiện việc\s+", ""),
    (r"\bthực hiện việc\s+", ""),
    (r"\btiến hành quá trình\s+", ""),
    (r"\bđưa ra kết luận khẳng định\b", "khẳng định"),
    (r"\bthực hiện phân tích\b", "phân tích"),
    (r"\bthực hiện tối ưu hóa\b", "tối ưu hóa"),
    (r"\bthực hiện khảo sát\b", "khảo sát"),
    
    # Weasel words & padding
    (r"\brất\s+", ""),
    (r"\bvô cùng\s+", ""),
    (r"\bcực kỳ\s+", ""),
    (r"\btương đối\s+", ""),
    (r"\bnhìn chung thì\s+", ""),
    (r"\brõ ràng là\s+", ""),
    (r"\bhiển nhiên là\s+", ""),
    (r"\bcó thể nói rằng\s+", ""),
    (r"\btrên thực tế thì\s+", ""),
    
    # Cliché phrases (anywhere in text)
    (r"\btrong bối cảnh( hiện nay| của thời đại số| 4\.0)?,?\s*", "", re.IGNORECASE),
    (r"\bkhông thể phủ nhận rằng,?\s*", "", re.IGNORECASE),
    (r"\bnhư chúng ta đã biết,?\s*", "", re.IGNORECASE),
    (r"\btóm lại, việc\s+", "Kết quả cho thấy ", re.IGNORECASE),
    (r"\bđóng vai trò (vô cùng )?(quan trọng|then chốt|không thể thiếu)\b", "ảnh hưởng trực tiếp", re.IGNORECASE),
    (r"\blà một bước tiến mang tính đột phá\b", "đạt hiệu quả thực nghiệm cao", re.IGNORECASE),
]

REPLACEMENTS_ENGLISH = [
    # Zombie nouns -> direct verbs
    (r"\bconduct(ed)? an analysis of\b", r"analyzed", re.IGNORECASE),
    (r"\bconduct(ed)? an investigation into\b", r"investigated", re.IGNORECASE),
    (r"\bconduct(ed)? an examination of\b", r"examined", re.IGNORECASE),
    (r"\bmake(s)? an assumption that\b", r"assumes that", re.IGNORECASE),
    (r"\bmade an assumption that\b", r"assumed that", re.IGNORECASE),
    (r"\bperform(ed)? a demonstration of\b", r"demonstrated", re.IGNORECASE),
    (r"\btake into consideration\b", r"consider", re.IGNORECASE),
    (r"\btaken into consideration\b", r"considered", re.IGNORECASE),
    
    # Weasels & filler throat-clearing
    (r"\bclearly\s+", "", re.IGNORECASE),
    (r"\bobviously\s+", "", re.IGNORECASE),
    (r"\bextremely\s+", "", re.IGNORECASE),
    (r"\bremarkably\s+", "", re.IGNORECASE),
    (r"\bvirtually\s+", "", re.IGNORECASE),
    (r"\bessentially\s+", "", re.IGNORECASE),
    (r"\bin a sense,?\s*", "", re.IGNORECASE),
    (r"\bit goes without saying that\s*", "", re.IGNORECASE),
    (r"\bit is important to remember that\s*", "Note that ", re.IGNORECASE),
    (r"\bit is worth noting that\s*", "Notably, ", re.IGNORECASE),
    (r"\bin today's (fast-paced|digital|modern) world,?\s*", "In modern practice, ", re.IGNORECASE),
    (r"\ba double-edged sword\b", "a systemic trade-off", re.IGNORECASE),
    (r"\bdelve into\b", "examine", re.IGNORECASE),
    (r"\bdelves into\b", "examines", re.IGNORECASE),
    (r"\btapestry of\b", "interplay of", re.IGNORECASE),
    (r"\bstands as a testament to\b", "confirms", re.IGNORECASE),
    (r"\bplays a crucial role in\b", "substantially improves", re.IGNORECASE),
    (r"\bfurthermore,?\s*", "Additionally, ", re.IGNORECASE),
    (r"\bmoreover,?\s*", "In turn, ", re.IGNORECASE),
]

def apply_mechanical_humanization(text: str) -> str:
    cleaned = text
    for item in REPLACEMENTS_VIETNAMESE + REPLACEMENTS_ENGLISH:
        pattern = item[0]
        repl = item[1]
        flags = item[2] if len(item) > 2 else 0
        cleaned = re.sub(pattern, repl, cleaned, flags=flags)
    
    # Clean up double spaces or awkward punctuation
    cleaned = re.sub(r'\s{2,}', ' ', cleaned)
    cleaned = re.sub(r'\s+([,.:;?!])', r'\1', cleaned)
    # Capitalize first letter of sentences
    sentences = re.split(r'([.!?]\s+)', cleaned)
    recapitalized = []
    for s in sentences:
        if s and s[0].islower():
            s = s[0].upper() + s[1:]
        recapitalized.append(s)
    return "".join(recapitalized).strip()

def main():
    if len(sys.argv) > 1:
        raw_text = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        raw_text = sys.stdin.read().strip()
    else:
        print("Usage: python humanize_text.py 'Đoạn văn bản cần tối ưu hóa...'")
        sys.exit(1)

    print("=" * 70)
    print("STEP 1: AUDITING ORIGINAL TEXT")
    print("=" * 70)
    report_orig = audit_academic_text(raw_text)
    print(f"Original Verdict   : {report_orig.get('verdict')}")
    print(f"Original AI Risk   : {report_orig.get('ai_risk_score')}")
    print(f"Original Burstiness: {report_orig.get('burstiness_index')}")
    print(f"Clichés Detected   : {report_orig.get('cliches_detected')}")
    print(f"Weasels Detected   : {report_orig.get('weasels_detected')}")
    print(f"Zombies Detected   : {report_orig.get('zombie_nouns_detected')}")

    print("\n" + "=" * 70)
    print("STEP 2: APPLYING MECHANICAL DE-AI TRANSFORMATIONS")
    print("=" * 70)
    humanized_text = apply_mechanical_humanization(raw_text)
    print("\n>>> PROPOSED HUMANIZED TEXT:\n")
    print(humanized_text)

    print("\n" + "=" * 70)
    print("STEP 3: RE-AUDITING HUMANIZED TEXT")
    print("=" * 70)
    report_new = audit_academic_text(humanized_text)
    print(f"New Verdict        : {report_new.get('verdict')}")
    print(f"New AI Risk        : {report_new.get('ai_risk_score')}")
    print(f"New Burstiness     : {report_new.get('burstiness_index')}")
    print(f"Clichés Remaining  : {report_new.get('cliches_detected')}")
    print(f"Weasels Remaining  : {report_new.get('weasels_detected')}")
    print(f"Zombies Remaining  : {report_new.get('zombie_nouns_detected')}")
    print("=" * 70)

if __name__ == "__main__":
    main()
