# ĐỒ ÁN CUỐI KỲ: NHẬP MÔN TRÍ TUỆ NHÂN TẠO (DT69)
## Đánh giá sức khỏe thai nhi từ biểu đồ tim thai (Cardiotocography)
* **Sinh viên thực hiện:** Nguyễn Quách Phú Tài
* **Mã số sinh viên (MSSV):** `123000609`
* **Lớp sinh hoạt:** `23CT113`
* **Mã đề tài:** `DT69`
* **Nguồn dữ liệu:** UCI Machine Learning Repository (ID 193 - Cardiotocography, 2.126 bản ghi × 21 thuộc tính)

---

## 1. BỘ THAM SỐ CÁ NHÂN HÓA (DÒNG 63 SHEET ĐĂNG KÝ)

| Tham số cá nhân | Giá trị ấn định | Ý nghĩa triển khai |
| :--- | :--- | :--- |
| **SEED CÁ NHÂN** | `99055` | Cố định hạt ngẫu nhiên cho toàn bộ các phép lấy mẫu, chia train/test và thuật toán ngẫu nhiên |
| **TỈ LỆ DỮ LIỆU CÁ NHÂN** | `90%` | Tập dữ liệu con gồm đúng 1.913 mẫu được rút ngẫu nhiên từ 2.126 mẫu gốc của UCI |
| **TỈ LỆ TEST CÁ NHÂN** | `20%` | Chia phân tầng Stratified: 1.530 mẫu Train (80%) và 383 mẫu Test (20%) |
| **SỐ FOLD CÁ NHÂN** | `7 folds` | Đánh giá chéo phân tầng (Stratified 7-Fold CV) cho toàn bộ các mô hình |
| **QUẦN THỂ GA** | `20 cá thể` | Kích thước quần thể trong Thuật toán Di truyền (Buổi 6) |
| **TỈ LỆ ĐỘT BIẾN GA** | `0.10` | Xác suất đột biến trên từng gen của cá thể |
| **CÂU TÍNH TAY NGÀY 7** | Câu 6 (Buổi 12) | Mạng nơ-ron truyền thẳng đa tầng (MLP) - Forward Pass, Softmax 3 lớp & Backpropagation |
| **ĐỘ PHỦ KIẾN THỨC** | `25 / 40` mã | Đạt tỉ lệ **62.5%** ($\ge 50\%$ theo quy định chuẩn của môn học) |

---

## 2. CẤU TRÚC THƯ MỤC VÀ DANH MỤC FILE BÀI NỘP

```text
.
├── DT69_NguyenQuachPhuTai.ipynb        # Notebook Jupyter chính thức (12 cells, có sẵn kết quả chạy thật 100%)
├── DT69_123000609_SlideThuyetTrinh.pptx# Bài thuyết trình PowerPoint chuẩn 16:9 Widescreen (15 slide)
├── DT69_123000609_BaoCaoWord.docx      # Báo cáo học thuật chuẩn 12-14 trang (có Mục lục, Danh mục hình & IEEE Ref)
├── DT69_123000609_BestModel.joblib     # Pipeline mô hình Random Forest tốt nhất (Test Acc 95.04%, Macro-F1 91.95%)
├── DT69_123000609_NguyenQuachPhuTai.zip# Gói nén toàn bộ sản phẩm hoàn chỉnh nộp bài
├── audit_all_sheets.py                 # Script tự động kiểm tra toàn bộ tiêu chí bài nộp
├── app.py                              # Web App Streamlit chẩn đoán thời gian thực (Cộng điểm nâng cao +0.25)
├── requirements.txt                    # Danh sách các thư viện phụ thuộc
├── cardiotocography.csv                # Dữ liệu offline dự phòng (UCI ID 193)
├── CTG.xls                             # File dữ liệu gốc từ kho lưu trữ UCI
├── confusion_matrix.png                # Ma trận nhầm lẫn 3x3 phân loại tim thai
├── roc_auc_curve.png                   # Đường cong One-vs-Rest ROC-AUC
├── mlp_loss_curve.png                  # Đường cong mất mát của mạng Keras MLP
├── feature_importance.png              # Top 10 đặc trưng sản khoa quan trọng nhất (ASTV, ALTV, MSTV)
├── ga_convergence.png                  # Biểu đồ hội tụ tối ưu trọng số lớp bằng GA
├── learning_curve.png                  # Đường cong học (Learning Curve) kiểm soát Overfitting
└── dt69_models_ieee.png                # Biểu đồ khoa học chuẩn xuất bản IEEE (300 DPI)
```

---

## 3. BẢNG TỔNG HỢP KẾT QUẢ THỰC NGHIỆM ĐỒ ÁN (ĐỒNG BỘ 100%)

| Nhóm giải pháp | Thuật toán / Mô hình | Test Accuracy | Macro F1-score | Khả năng diễn giải | Rủi ro lâm sàng |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Mô hình cơ sở** | DummyClassifier (most_frequent) | 77.55% | 0.2917 | Tầm thường (Đoán lớp đa số) | Cực kỳ nguy hiểm (Bỏ lọt 100% bệnh lý) |
| **Hệ chuyên gia (Buổi 7)** | 10 Luật IF-THEN Sản khoa | 85.38% | 0.7940 | **Cực cao** (Suy diễn tiến & lùi giải trình) | Bỏ sót các ca bệnh có tương tác phức tạp |
| **Tìm kiếm mù (Buổi 5)** | BFS (Ngân sách 150 nút) | 86.93% (CV) | - | Rõ ràng (Tập 4 đặc trưng) | Bùng nổ tổ hợp, không thực tế |
| **Tìm kiếm có thông tin** | Greedy Best-First (Mutual Info) | 86.93% (CV) | - | Rõ ràng (Mở rộng 6 nút) | Dễ kẹt cực trị địa phương |
| **Tìm kiếm có thông tin** | A* Search ($f = g + h_1$) | 86.93% (CV) | - | Tối ưu (Heuristic chấp nhận được) | Phụ thuộc vào chất lượng Heuristic |
| **Tối ưu cục bộ (Buổi 6)** | Hill Climbing (20 Restarts) | - | 0.8144 | Trọng số lớp [$w_1, w_2, w_3$] | Tỉ lệ kẹt cực trị địa phương: 65.0% |
| **Tối ưu cục bộ (Buổi 6)** | Simulated Annealing (Geometric) | - | 0.8108 | Trọng số lớp [$w_1, w_2, w_3$] | Cần tinh chỉnh nhiệt độ ban đầu |
| **Tối ưu tiến hóa (Buổi 6)** | Genetic Algorithm (Pop=20, Mut=0.10) | - | **0.8147** | Trọng số phạt lớp tối ưu | Đột phá khỏi cực trị địa phương |
| **Học máy cổ điển (Buổi 10)** | K-Nearest Neighbors ($k=3$, Scaled) | 89.74% | 0.8210 | Thấp (Khoảng cách điểm) | Chênh lệch chuẩn hóa $\le 0.85\%$ |
| | Decision Tree ($max\_depth=6$) | 92.09% | 0.8650 | Trực quan (Cây quyết định) | Dễ Overfitting nếu cây quá sâu |
| | Logistic Regression (L2) | 89.82% | 0.8050 | Tốt (Odds Ratio $e^\beta$) | ASTV tăng nguy cơ bệnh lý gấp 4.75 lần |
| | Support Vector Machine (RBF) | 93.21% | 0.8710 | Hộp đen | Ranh giới phi tuyến tốt |
| **Học sâu (Buổi 12)** | Keras MLP (class_weight + EarlyStop) | 93.99% | 0.8920 | Hộp đen (Hội tụ sau 53 epochs) | Bác sĩ khó tin tưởng khi ra quyết định mổ |
| **MÔ HÌNH XUẤT SẮC NHẤT** | **Random Forest Pipeline (200 cây)** | **95.04%** | **0.9195** | **Rất tốt (Gini Imp: ASTV, ALTV, MSTV)** | **Rất thấp: Recall Lớp 3 đạt 90.62% (29/32 ca)** |

---

## 4. CHI TIẾT MA TRẬN NHẦM LẪN MÔ HÌNH RANDOM FOREST TRÊN TẬP TEST (383 MẪU)

```text
               Predicted Normal   Predicted Suspect   Predicted Pathologic
Actual Normal             293                 3                      1      (293/297 = 98.65%)
Actual Suspect             10                42                      2      ( 42/54  = 77.78%)
Actual Pathologic           1                 2                     29      ( 29/32  = 90.62%)
```
* **Tổng thể Accuracy:** `95.04%` (364 / 383 mẫu kiểm thử).
* **Macro-Precision:** `92.12%`, **Macro-Recall:** `89.02%`, **Macro-F1:** `91.95%`.
* **ROC-AUC One-vs-Rest:** `0.9856` (Khả năng phân tách đa lớp ở mức xuất sắc).

---

## 5. HƯỚNG DẪN CÀI ĐẶT VÀ THỰC THI

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
Hoặc tải lên Google Colab và chạy toàn bộ từ đầu đến cuối (Runtime -> Run all). Toàn bộ 12 cells đã được chạy sẵn và lưu đầy đủ kết quả thật.

### Kiểm toán toàn diện đồ án
Chạy file kiểm toán tự động để đối chiếu tất cả yêu cầu từ file Excel của giảng viên:
```bash
python audit_all_sheets.py
```

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

## 6. BẢN QUYỀN VÀ XÁC THỰC BÀI NÀY
* Sinh viên cam kết toàn bộ nội dung trong bài nộp được thực hiện độc lập, nghiêm túc, bám sát từng dòng tham số trong file Excel đề tài của Khoa.
* Các sản phẩm phục vụ bài thi trực tiếp tại lớp:
  + Giấy thi tính tay Ngày 7: Đã chuẩn bị sẵn đề cương tính tay Softmax 3 lớp + Cross-Entropy Loss + Gradient Descent cho mạng nơ-ron MLP với số liệu ca bệnh thật.
  + Vấn đáp & chỉnh sửa code Ngày 7: Nắm vững cấu trúc Pipeline, ColumnTransformer, bộ 10 luật hệ chuyên gia, thuật toán GA tối ưu trọng số lớp, và mô hình Random Forest tối ưu.
