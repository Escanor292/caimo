# CẨM NANG HƯỚNG DẪN KHÁM PHÁ BỘ SKILLS TOOLKIT
## Toàn bộ công cụ Viết học thuật chống AI & Xuất bản Báo cáo / Slide / Sơ đồ

Thư mục này được copy trực tiếp ra thư mục làm việc chính [`d:\AI-20261107T093517Z-1-001\AI\SKILLS_TOOLKIT\`](file:///d:/AI-20261107T093517Z-1-001/AI/SKILLS_TOOLKIT) để bạn dễ dàng mở xem từng file, chạy thử nghiệm và kiểm tra xem mọi thứ hoạt động thế nào.

---

## 📁 CẤU TRÚC CHI TIẾT TỪNG THƯ MỤC VÀ TỪNG FILE

```text
SKILLS_TOOLKIT/
│
├── 01_AI_Text_Humanizer/                 <-- BỘ 1: VIẾT HỌC THUẬT & CHỐNG MÁY QUÉT AI (Turnitin/GPTZero)
│   ├── SKILL.md                          <-- Quy trình khép kín 3 bước: Viết -> Soi linter -> Tự sửa
│   ├── references/
│   │   ├── academic_humanizer_rules.md   <-- CỰC QUAN TRỌNG: Danh mục từ cấm (delve, tapestry, trong bối cảnh...) & quy tắc DIPPER
│   │   ├── zero_shot.md                  <-- Lý thuyết về Binoculars, DetectGPT, Fast-DetectGPT, GLTR
│   │   ├── supervised.md                 <-- Lý thuyết về DeBERTa-v3 (Desklib), PhoBERT tiếng Việt
│   │   └── benchmarks_and_watermarking.md<-- Lý thuyết về MAGE, MGTBench, LM-Watermarking
│   └── scripts/
│       ├── text_stats.py                 <-- CÔNG CỤ 1: Máy soi chữ ký AI (Đo Burstiness, AI Risk 0-100%, linter)
│       ├── humanize_text.py              <-- CÔNG CỤ 2: Tự động gọt hư từ đệm, khử danh từ hóa, hạ điểm AI
│       └── detect_hf_api.py              <-- CÔNG CỤ 3: Gọi Hugging Face API cho các mô hình online
│
└── 02_Academic_Report_and_Slides/        <-- BỘ 2: VẼ SƠ ĐỒ, BIỂU ĐỒ IEEE & TỰ ĐỘNG XUẤT BÁO CÁO/SLIDE
    ├── SKILL.md                          <-- Hướng dẫn tự động hóa báo cáo và bài thuyết trình
    ├── references/
    │   ├── diagrams_as_code.md           # Mermaid.js, mingrammer/diagrams, D2, PlantUML, Excalidraw
    │   ├── scientific_plotting.md        # SciencePlots (IEEE/Nature/Science), PlotNeuralNet, ECharts
    │   ├── slide_automation.md           # python-pptx, Marp CLI, Slidev, Reveal.js
    │   └── academic_publishing.md        # python-docx, Typst, Quarto, Pandoc
    └── scripts/
        ├── make_ieee_plot.py             <-- CÔNG CỤ 4: Xuất biểu đồ chuẩn bài báo quốc tế IEEE (300 DPI & PDF)
        ├── build_academic_doc.py         <-- CÔNG CỤ 5: Tự động tạo file Word (.docx) chuẩn cấu trúc trường ĐH
        ├── build_deck_pptx.py            <-- CÔNG CỤ 6: Tự động tạo bộ Slide thuyết trình 16:9 (.pptx)
        └── render_mermaid.py             <-- CÔNG CỤ 7: Biên dịch sơ đồ Mermaid sang ảnh PNG/SVG
```

---

## 🚀 CÁCH CHẠY THỬ NGAY TỪNG CÔNG CỤ ĐỂ KIỂM TRA

Mở PowerShell tại thư mục `d:\AI-20261107T093517Z-1-001\AI` và copy-paste các lệnh sau để trải nghiệm trực tiếp:

### 1. Test Bộ Soi Lỗi Văn Phong AI (`text_stats.py`)
Kiểm tra xem một đoạn văn có bị Turnitin / GPTZero gắn cờ không:
```powershell
python SKILLS_TOOLKIT/01_AI_Text_Humanizer/scripts/text_stats.py "Trong bối cảnh hiện nay, trí tuệ nhân tạo đóng vai trò vô cùng quan trọng. Không thể phủ nhận rằng công nghệ này phát triển nhanh chóng. Tóm lại, việc ứng dụng AI là một bước tiến mang tính đột phá."
```
*(Kết quả sẽ báo đỏ `FAILED` ngay lập tức, chỉ ra 5 cụm từ sáo rỗng và nhịp câu quá đều).*

---

### 2. Test Bộ Tự Động Làm Sạch & Hạ Điểm AI (`humanize_text.py`)
Tự động dọn rác, khử danh từ hóa và hạ điểm AI:
```powershell
python SKILLS_TOOLKIT/01_AI_Text_Humanizer/scripts/humanize_text.py "It is important to remember that we conducted an investigation into the algorithm."
```
*(Kết quả sẽ tự động đổi câu thành: "Note that we investigated the algorithm." và hạ điểm rủi ro AI).*

---

### 3. Test Bộ Xuất Biểu Đồ Chuẩn IEEE (`make_ieee_plot.py`)
Vẽ biểu đồ hội tụ thuật toán chuẩn mực tạp chí quốc tế Nature / IEEE:
```powershell
python SKILLS_TOOLKIT/02_Academic_Report_and_Slides/scripts/make_ieee_plot.py --output "bieu_do_test_ieee.png"
```
*(Tạo ra 1 file ảnh `bieu_do_test_ieee.png` 300 DPI và 1 file vector `bieu_do_test_ieee.pdf` nét căng).*

---

### 4. Test Bộ Tự Động Sinh Báo Cáo Word (.docx) (`build_academic_doc.py`)
Tự động tạo khung báo cáo khóa luận / đồ án chuẩn trường đại học:
```powershell
python SKILLS_TOOLKIT/02_Academic_Report_and_Slides/scripts/build_academic_doc.py --output "BaoCao_Mau_Moi.docx"
```
*(Mở file `BaoCao_Mau_Moi.docx` lên xem: Đã có sẵn trang bìa chuẩn, định dạng heading 1/2/3, lề 2.5cm, bảng số liệu có tiêu đề).*

---

### 5. Test Bộ Tự Động Sinh Slide PowerPoint 16:9 (.pptx) (`build_deck_pptx.py`)
Tự động dựng slide thuyết trình chuyên nghiệp:
```powershell
python SKILLS_TOOLKIT/02_Academic_Report_and_Slides/scripts/build_deck_pptx.py --output "Slide_Mau_Moi.pptx"
```
*(Mở file `Slide_Mau_Moi.pptx` lên xem: Đã có slide bìa màu xanh Navy sang trọng, lộ trình trình bày 5 mục, bảng kết quả số liệu).*
