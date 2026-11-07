# ĐỒ ÁN CUỐI KỲ: NHẬP MÔN TRÍ TUỆ NHÂN TẠO (DT69)
## Đánh giá sức khỏe thai nhi từ biểu đồ tim thai (Cardiotocography)
* **Sinh viên thực hiện:** Nguyễn Quách Phú Tài
* **Mã số sinh viên (MSSV):** `123000609`
* **Lớp sinh hoạt:** `23CT113`
* **Mã đề tài:** `DT69`
* **Nguồn dữ liệu:** UCI Machine Learning Repository (ID 193 - Cardiotocography, 2.126 bản ghi × 21 thuộc tính)

---

## 1. BỘ THAM SỐ CÁ NHÂN HÓA (DÒNG 29 SHEET ĐĂNG KÝ)

| Tham số cá nhân | Giá trị ấn định | Ý nghĩa triển khai |
| :--- | :--- | :--- |
| **SEED CÁ NHÂN** | `99055` | Cố định hạt ngẫu nhiên cho toàn bộ các phép lấy mẫu, chia train/test và thuật toán ngẫu nhiên |
| **TỈ LỆ DỮ LIỆU CÁ NHÂN** | `90%` | Tập dữ liệu con gồm 1.913 mẫu được rút từ 2.126 mẫu gốc của UCI |
| **TỈ LỆ TEST CÁ NHÂN** | `20%` | Chia phân tầng Stratified: 1.530 mẫu Train (80%) và 383 mẫu Test (20%) |
| **SỐ FOLD CÁ NHÂN** | `7 folds` | Đánh giá chéo phân tầng (Stratified 7-Fold CV) cho toàn bộ các mô hình |
| **QUẦN THỂ GA** | `20 cá thể` | Kích thước quần thể khởi tạo trong Giải thuật Di truyền (Buổi 6) |
| **TỈ LỆ ĐỘT BIẾN GA** | `0.10` | Xác suất đảo bit đột biến trên từng gen của cá thể |
| **CÂU TÍNH TAY NGÀY 7** | Câu 6 (Buổi 12) | Mạng nơ-ron truyền thẳng đa tầng (MLP) - Forward Pass & Backpropagation |

---

## 2. CẤU TRÚC THƯ MỤC VÀ DANH MỤC FILE BÀI NỘP

```text
.
├── DT69_NguyenQuachPhuTai.ipynb        # Notebook Jupyter chính thức (12 cells, có sẵn kết quả chạy thật)
├── DT69_123000609_SlideThuyetTrinh.pptx# Bài thuyết trình PowerPoint chuẩn 15 slide (12-18 slide limit)
├── DT69_123000609_BaoCaoWord.docx      # Báo cáo học thuật chuẩn 12-13 trang (10-15 trang limit)
├── DT69_123000609_BestModel.joblib     # Pipeline mô hình Random Forest tốt nhất (Test Acc 95.04%)
├── app.py                              # Web App Streamlit chẩn đoán thời gian thực (Cộng điểm nâng cao +0.25)
├── requirements.txt                    # Danh sách các thư viện phụ thuộc
├── confusion_matrix.png                # Ma trận nhầm lẫn 3x3 phân loại tim thai
├── roc_auc_curve.png                   # Đường cong One-vs-Rest ROC-AUC
├── mlp_loss_curve.png                  # Đường cong hội tụ Loss của mạng MLP
├── feature_importance.png              # Top 10 đặc trưng sản khoa quan trọng nhất
├── ga_convergence.png                  # Biểu đồ so sánh hội tụ: Hill Climbing vs SA vs GA
│
└── .agents/skills/ai-text-detection/   # Trợ lý Viết học thuật & Humanizer chống AI (Turnitin/GPTZero)
    ├── SKILL.md                        # Quy trình 3 bước khép kín Write -> Audit -> Humanize
    ├── references/
    │   └── academic_humanizer_rules.md # Cẩm nang DIPPER, Proselint, Write-Good & Banned Clichés
    └── scripts/
        ├── text_stats.py               # Linter soi chữ ký AI (Burstiness, AI Risk 0-100%, Weasels, Zombies)
        └── humanize_text.py            # Script tự động khử danh từ hóa và hư từ đệm
```

---

## 3. BẢNG TỔNG HỢP KẾT QUẢ THỰC NGHIỆM

| Nhóm giải pháp | Thuật toán / Mô hình | Test Accuracy | Macro F1-score | Khả năng diễn giải |
| :--- | :--- | :---: | :---: | :--- |
| **Mô hình cơ sở** | DummyClassifier (Stratified) | 64.49% | 0.3321 | Kém (Đoán ngẫu nhiên theo phân bố nhãn) |
| **Hệ chuyên gia (Buổi 7)** | 10 Luật IF-THEN Sản khoa | 82.25% | 0.7410 | **Cực cao** (Suy diễn tiến & lùi giải thích được từng ca) |
| **Tìm kiếm có thông tin (Buổi 5)** | A* Feature Selection ($f=g+h$) | 87.21% | 0.8105 | Rõ ràng (Rút gọn từ 21 xuống 4 chỉ số cốt lõi) |
| **Tối ưu hóa cục bộ (Buổi 6)** | GA (Pop=20, Mut=0.10) | 90.45% | 0.8520 | Tối ưu hóa tổ hợp đặc trưng vượt trội Hill Climbing |
| **Học máy phân loại (Buổi 10)** | Logistic Regression (L2) | 88.51% | 0.7984 | Cao (Đọc được trọng số hệ số Odds Ratio) |
| | Decision Tree (max_depth=5) | 91.12% | 0.8412 | Cao (Trực quan hóa cây quyết định) |
| | K-Nearest Neighbors ($k=5$) | 89.82% | 0.8250 | Trung bình |
| **Mạng nơ-ron (Buổi 12)** | MLP Keras (EarlyStopping + L2) | 88.51% | 0.8240 | Hộp đen (Hội tụ sau 42 epochs) |
| **MÔ HÌNH TỐT NHẤT** | **Random Forest (150 trees)** | **95.04%** | **0.9015** | **Xuất sắc (Feature Importances: ASTV, ALTV, Mean)** |

---

## 4. HƯỚNG DẪN CÀI ĐẶT VÀ THỰC THI

### Cài đặt môi trường
Khuyến nghị sử dụng Python 3.10 trở lên:
```bash
pip install -r requirements.txt
```

### Chạy Notebook
Mở bằng Jupyter Notebook, JupyterLab hoặc VS Code:
```bash
jupyter notebook DT69_NguyenQuachPhuTai.ipynb
```
Hoặc tải lên Google Colab và chạy toàn bộ từ đầu đến cuối (Runtime -> Run all).

### Chạy ứng dụng Web Demo (Streamlit)
Khởi chạy giao diện chẩn đoán tương tác dành cho bác sĩ sản khoa:
```bash
streamlit run app.py
```
Giao diện sẽ tự động mở trên trình duyệt tại địa chỉ `http://localhost:8501`.

### Nạp lại mô hình đã đóng gói
```python
import joblib, pandas as pd

# Nạp pipeline hoàn chỉnh
model = joblib.load("DT69_123000609_BestModel.joblib")

# Dự đoán mẫu CTG mới (chỉ cần truyền DataFrame 21 thuộc tính)
sample = pd.DataFrame([{
    'LB': 130.0, 'AC': 3.0, 'FM': 0.0, 'UC': 2.0, 'DL': 0.0, 'DS': 0.0, 'DP': 0.0,
    'ASTV': 25.0, 'MSTV': 1.8, 'ALTV': 0.0, 'MLTV': 10.5, 'Width': 60.0, 'Min': 100.0,
    'Max': 160.0, 'Nmax': 3.0, 'Nzeros': 0.0, 'Mode': 135.0, 'Mean': 133.0,
    'Median': 134.0, 'Variance': 10.0, 'Tendency': 0.0
}])

prediction = model.predict(sample) # 1: Bình thường, 2: Nghi ngờ, 3: Bệnh lý
print("Kết quả chẩn đoán:", prediction[0])
```

---

## 5. CÔNG CỤ TRỢ LÝ VIẾT HỌC THUẬT (AI TEXT HUMANIZER)

Thư mục `.agents/skills/ai-text-detection/` chứa công cụ kiểm toán văn phong học thuật chống máy quét AI (Turnitin, GPTZero):

* **Kiểm tra độ rủi ro AI & nhịp câu của đoạn văn:**
  ```bash
  python .agents/skills/ai-text-detection/scripts/text_stats.py "Đoạn văn bản cần kiểm tra..."
  ```
* **Tự động làm sạch từ đệm và khử danh từ hóa:**
  ```bash
  python .agents/skills/ai-text-detection/scripts/humanize_text.py "Đoạn văn bản cần làm sạch..."
  ```


---

## 6. CÔNG CỤ VẼ SƠ ĐỒ, BIỂU ĐỒ KHOA HỌC & LÀM SLIDE (ACADEMIC REPORT & SLIDES)

Thư mục `.agents/skills/academic-report-and-slides/` cung cấp bộ công cụ tự động hóa toàn diện cho báo cáo học thuật:

* **Vẽ biểu đồ khoa học chuẩn IEEE / Nature (300 DPI):**
  ```bash
  python .agents/skills/academic-report-and-slides/scripts/make_ieee_plot.py --output "my_chart.png"
  ```
* **Tự động tạo khung báo cáo Word chuẩn trường đại học (.docx):**
  ```bash
  python .agents/skills/academic-report-and-slides/scripts/build_academic_doc.py --output "BaoCao_Moi.docx"
  ```
* **Tự động tạo bộ Slide thuyết trình 16:9 (.pptx):**
  ```bash
  python .agents/skills/academic-report-and-slides/scripts/build_deck_pptx.py --output "Slide_Moi.pptx"
  ```
* **Biên dịch sơ đồ Mermaid sang ảnh PNG độ nét cao:**
  ```bash
  python .agents/skills/academic-report-and-slides/scripts/render_mermaid.py "flowchart TD; A-->B;" -o "diagram.png"
  ```
