# Academic Presentation & Slide Automation Manual

This manual covers automated generation of professional academic and technical slides (16:9 widescreen, typography hierarchy, code syntax highlighting, embedded diagrams).

---

## 1. python-pptx (Programmatic PowerPoint Generation)

* **Repository:** [scanny/python-pptx](https://github.com/scanny/python-pptx)
* **Installation:** `pip install python-pptx`
* **Strength:** Native `.pptx` generation. Fully editable by users in PowerPoint / Google Slides / Keynote. Exact millimeter control over shapes, text frames, tables, and images.

### Production Template Architecture (16:9 Widescreen):
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5) # Standard 16:9 Widescreen

# Professional Palette
PRIMARY = RGBColor(24, 43, 73)      # Dark Navy
ACCENT = RGBColor(220, 53, 69)      # Crimson Red
TEXT_DARK = RGBColor(40, 40, 40)    # Charcoal
BG_LIGHT = RGBColor(248, 249, 250)  # Off-white

# Helper to create clean slide with header
def add_content_slide(prs, title_text, subtitle_text=""):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    
    # Title Box
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.2))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    
    if subtitle_text:
        p2 = tf.add_paragraph()
        p2.text = subtitle_text
        p2.font.size = Pt(14)
        p2.font.color.rgb = RGBColor(120, 120, 120)
    return slide
```

---

## 2. Marp (Markdown-to-Presentation CLI)

* **Repository:** [marp-team/marp](https://github.com/marp-team/marp)
* **CLI:** `@marp-team/marp-cli` via npx
* **Compilation Command:**
```bash
# Export directly to PowerPoint PPTX (editable):
npx @marp-team/marp-cli slides.md -o presentation.pptx

# Export directly to PDF:
npx @marp-team/marp-cli slides.md -o presentation.pdf --allow-local-files
```

### Marp Markdown Syntax:
```markdown
---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f5f5f5
---

# ĐỒ ÁN CUỐI KỲ: AI IN HEALTHCARE
## Đánh giá sức khỏe thai nhi từ biểu đồ tim thai (DT69)
**Nguyễn Quách Phú Tài - MSSV: 123000609**

---

## 1. Đặt vấn đề & Mục tiêu
- **Bối cảnh:** Hơn 2 triệu ca thai chết lưu mỗi năm trên toàn cầu do thiếu oxy cấp trong chuyển dạ.
- **Dữ liệu:** UCI ID 193 gồm 2.126 bản ghi với 21 chỉ số đo lường.
- **Mục tiêu:** Phân loại 3 nhóm trạng thái:
  1. Bình thường (Normal)
  2. Nghi ngờ (Suspect)
  3. Bệnh lý (Pathologic)

---

## 2. Kết quả Thực nghiệm

| Mô hình | Test Accuracy | Macro F1-score |
| :--- | :---: | :---: |
| Hệ chuyên gia (10 Luật) | 82.25% | 0.7410 |
| Mạng Nơ-ron (MLP) | 88.51% | 0.8240 |
| **Random Forest (Best)** | **95.04%** | **0.9015** |
```

---

## 3. Slidev (Interactive Developer & Academic Presentations)

* **Repository:** [slidevjs/slidev](https://github.com/slidevjs/slidev)
* **Best For:** Technical talks with live code execution, Shiki syntax highlighting, interactive Mermaid diagrams, and LaTeX math formulas.

---

## 4. Reveal.js (HTML5 Presentations)

* **Repository:** [hakimel/reveal.js](https://github.com/hakimel/reveal.js)
* **Best For:** Standalone browser-based presentations with 3D transitions, speaker view notes, and dynamic JSON charts.
