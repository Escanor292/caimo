# Multi-Format Academic Report Publishing

This manual covers automated document generation across Word (`.docx`), PDF via Typst / LaTeX, and Markdown via Quarto and Pandoc.

---

## 1. python-docx (Programmatic Word Report Generation)

* **Repository:** [python-openxml/python-docx](https://github.com/python-openxml/python-docx)
* **Installation:** `pip install python-docx`
* **Best For:** Creating standardized university reports matching institution guidelines (margins, font styles, cover pages, tables, figure captions).

### University Formatting Standard Recipe:
* **Margins:** 2.5 cm (1 inch) on all sides (or Left 3.0 cm, Right 2.0 cm, Top 2.0 cm, Bottom 2.0 cm for binding).
* **Typography:** Times New Roman (13 pt or 12 pt), 1.5 or 1.15 line spacing, 6 pt after paragraphs.
* **Heading Hierarchy:**
  * Heading 1: 16 pt, Bold, ALL CAPS, Navy Blue (`#1a365d`)
  * Heading 2: 14 pt, Bold, Title Case
  * Heading 3: 13 pt, Italic Bold
* **Tables:** Header row highlighted with brand color (`#1a365d`), text white bold; alternating row shading (`#f8f9fa`); borders subtle gray (`#d1d5db`).
* **Captions:**
  * Tables: Caption placed **above** the table (*Bảng 1: ...*).
  * Figures: Caption placed **below** the figure (*Hình 1: ...*).

---

## 2. Typst (Modern Blazing-Fast Replacement for LaTeX)

* **Repository:** [typst/typst](https://github.com/typst/typst)
* **Why Typst:** Compiles in **< 30 milliseconds** (instant preview), syntax as simple as Markdown, produces typography identical to or better than LaTeX, native table of contents, BibTeX support.

### Typst University Report Template (`report.typ`):
```typst
#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 3cm, right: 2cm),
  header: align(right, text(8pt, fill: luma(120))[Đồ án Cuối kỳ - Nhập môn Trí tuệ Nhân tạo]),
  footer: locate(loc => align(center, text(10pt)[#loc.page()]))
)
#set text(font: "Times New Roman", size: 12pt, lang: "vi")
#set par(justify: true, leading: 0.8em)

// Cover Page
#align(center)[
  #text(14pt, weight: "bold")[TRƯỜNG ĐẠI HỌC ...]\
  #text(12pt)[KHOA CÔNG NGHỆ THÔNG TIN]\
  #v(3cm)
  #text(20pt, weight: "bold", fill: rgb("#1a365d"))[BÁO CÁO ĐỒ ÁN CUỐI KỲ]\
  #v(0.5cm)
  #text(16pt, weight: "bold")[ĐÁNH GIÁ SỨC KHỎE THAI NHI TỪ BIỂU ĐỒ TIM THAI]\
  #v(4cm)
  #align(left)[
    #text(12pt)[*Sinh viên thực hiện:* Nguyễn Quách Phú Tài]\
    #text(12pt)[*Mã số sinh viên:* 123000609]\
    #text(12pt)[*Lớp sinh hoạt:* 23CT113]\
    #text(12pt)[*Mã đề tài:* DT69]
  ]
]

#pagebreak()
#outline(title: "MỤC LỤC", indent: auto)
#pagebreak()

= 1. TỔNG QUAN ĐỀ TÀI
Biểu đồ tim thai (Cardiotocography - CTG) là phương tiện chẩn đoán sản khoa thiết yếu...
```

---

## 3. Quarto (Multi-Format Scientific Publishing)

* **Repository:** [quarto-dev/quarto-cli](https://github.com/quarto-dev/quarto-cli)
* **Strength:** Single source of truth. Writes text, embedded Python code, generates plots, and exports to `.docx`, `.pdf` (LaTeX), and `.pptx` simultaneously:
```bash
# Render to Word:
quarto render report.qmd --to docx

# Render to PDF:
quarto render report.qmd --to pdf

# Render to Presentation:
quarto render slides.qmd --to pptx
```

---

## 4. Pandoc (The Universal Document Converter)

* **Repository:** [jgm/pandoc](https://github.com/jgm/pandoc)
* **Useful Command:**
```bash
# Convert Markdown report to Word with University custom template:
pandoc report.md -o Final_Report.docx --reference-doc=University_Template.docx --toc
```
