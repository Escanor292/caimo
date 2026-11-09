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
| **TỈ LỆ DỮ LIỆU CÁ NHÂN** | `90%` | Tập dữ liệu con gồm đúng 1913 mẫu được rút ngẫu nhiên từ 2.126 mẫu gốc của UCI |
| **TỈ LỆ TEST CÁ NHÂN** | `20%` | Chia phân tầng Stratified: 1530 mẫu Train (80%) và 383 mẫu Test (20%) |
| **SỐ FOLD CÁ NHÂN** | `7 folds` | Đánh giá chéo phân tầng (Stratified 7-Fold CV) cho toàn bộ các mô hình |
| **QUẦN THỂ GA** | `20 cá thể` | Kích thước quần thể trong Thuật toán Di truyền (Buổi 6) |
| **TỈ LỆ ĐỘT BIẾN GA** | `0.10` | Xác suất đột biến trên từng gen của cá thể |
| **CÂU TÍNH TAY NGÀY 7** | Câu 6 (Buổi 12) | Mạng nơ-ron truyền thẳng đa tầng (MLP) - Forward Pass, Softmax 3 lớp & Backpropagation |
| **ĐỘ PHỦ KIẾN THỨC** | `25 / 40 (62.5%)` | Đạt tỉ lệ **62.5%** ($\ge 50\%$ theo quy định chuẩn của môn học) |

---

## 2. CẤU TRÚC THƯ MỤC VÀ DANH MỤC FILE BÀI NỘP

```text
.
├── DT69_NguyenQuachPhuTai.ipynb        # Notebook Jupyter chính thức (12 cells, có sẵn kết quả chạy thật 100%)
├── DT69_123000609_SlideThuyetTrinh.pptx # Bài thuyết trình PowerPoint 16:9 chính thức (15 slide, nhúng hình thật)
├── DT69_123000609_BaoCaoWord.docx      # Báo cáo học thuật chuẩn 12-14 trang (có Mục lục, 7 hình ảnh nhúng & IEEE Ref)
├── DT69_123000609_BestModel.joblib     # Pipeline mô hình Random Forest tốt nhất (Test Acc 95.04%, Macro-F1 90.43%)
├── exact_metrics.json                  # Single Source of Truth chứa toàn bộ chỉ số thực nghiệm chuẩn xác
├── app.py                              # Web App Streamlit chẩn đoán thời gian thực (Cộng điểm nâng cao +0.25)
├── README.md                           # Hướng dẫn chi tiết đồ án & đồng bộ số liệu thực nghiệm
├── requirements.txt                    # Danh sách các thư viện phụ thuộc
├── audit_all_sheets.py                 # Script tự động kiểm tra toàn bộ tiêu chí bài nộp
├── cardiotocography.csv                # Dữ liệu offline dự phòng (UCI ID 193)
├── CTG.xls                             # File dữ liệu gốc từ kho lưu trữ UCI
├── confusion_matrix.png                # Ma trận nhầm lẫn 3x3 phân loại tim thai
├── roc_auc_curve.png                   # Đường cong One-vs-Rest ROC-AUC (AUC 0.9919)
├── mlp_loss_curve.png                  # Đường cong mất mát của mạng Keras MLP
├── feature_importance.png              # Top 10 đặc trưng sản khoa quan trọng nhất (ASTV, ALTV, MSTV)
├── ga_convergence.png                  # Biểu đồ hội tụ tối ưu trọng số lớp bằng GA
├── learning_curve.png                  # Đường cong học (Learning Curve) kiểm soát Overfitting
├── dt69_models_ieee.png                # Biểu đồ cột khoa học chuẩn xuất bản IEEE (PNG 300 DPI)
└── dt69_models_ieee.pdf                # Biểu đồ định dạng vector PDF chất lượng cao
```

---

## 3. THÍ NGHIỆM ĐỐI CHỨNG RÒ RỈ DỮ LIỆU (CELL 4)

| Cấu hình thí nghiệm | Mô hình kiểm thử | Biến đầu vào | Test Accuracy | Ý nghĩa lâm sàng |
| :--- | :--- | :--- | :---: | :--- |
| **Có biến CLASS (Rò rỉ)** | Decision Tree | 21 chỉ số CTG + Cột CLASS | `98.43%` | Độ chính xác ảo (CLASS mã hóa phân loại của bác sĩ sau sinh) |
| **Không dùng CLASS (Chuẩn sạch)** | Decision Tree | Duy nhất 21 chỉ số đo đạc CTG | `93.99%` | Baseline thực tế, khách quan và an toàn |
| **Pipeline tối ưu cuối kỳ** | Random Forest Pipeline | 21 chỉ số CTG (Dữ liệu sạch) | **`95.04%`** | **Mô hình xuất sắc nhất, Macro-F1 90.43%** |

---

## 4. BẢNG TỔNG HỢP KẾT QUẢ THỰC NGHIỆM ĐỒ ÁN (ĐỒNG BỘ 100% VỚI OUTPUT NOTEBOOK)

| Nhóm giải pháp | Thuật toán / Mô hình | Test Accuracy | Macro F1-score | Khả năng diễn giải | Rủi ro lâm sàng |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Mô hình cơ sở** | DummyClassifier (most_frequent) | 77.55% | 0.2912 | Tầm thường (Đoán lớp đa số) | Cực kỳ nguy hiểm (Bỏ lọt 100% bệnh lý) |
| **Hệ chuyên gia (Buổi 7)** | 10 Luật IF-THEN (Suy diễn lùi) | 85.12% | 0.7066 | Rất cao (Giải trình chuỗi luật) | Bỏ sót các ca tương tác phi tuyến phức tạp |
| **Tìm kiếm mù (Buổi 5)** | BFS (150 nút chạm ngưỡng) | 91.57% (CV) | - | Rõ ràng (Tập 4 biến: MSTV, ASTV, ALTV, Mean) | Bùng nổ tổ hợp, không khả thi khi dữ liệu lớn |
| **Tìm kiếm Heuristic** | Greedy Best-First (MI - 6 nút) | 86.93% (CV) | - | Rõ ràng (Tập 4 biến: MSTV, Mean, Median, Min) | Dễ bị kẹt ở cực trị địa phương |
| **Tìm kiếm Heuristic** | Greedy Best-First (Custom - 6 nút) | 86.93% (CV) | - | Rõ ràng (Tập 4 biến) | Dễ bị kẹt ở cực trị địa phương |
| **Tìm kiếm tối ưu (Buổi 5)** | A* Search (g + h1 - 6 nút) | 86.93% (CV) | - | Tối ưu (Tiết kiệm gấp 25 lần số nút BFS) | Phụ thuộc chất lượng hàm Heuristic |
| **Tối ưu cục bộ (Buổi 6)** | Hill Climbing (20 Restarts) | - | 0.8132 | Trọng số lớp tường minh: [1.0, 2.25, 1.81] | Tỉ lệ kẹt cực trị địa phương cao (60.0%) |
| **Tối ưu làm nguội** | Simulated Annealing (Hình học) | - | 0.7901 | Trọng số phạt: [1.0, 2.78, 6.88] | Cần tinh chỉnh nhiệt độ ban đầu |
| **Tối ưu làm nguội** | Simulated Annealing (Tuyến tính) | - | 0.8095 | Trọng số phạt: [1.0, 2.93, 2.94] | Làm nguội đều đặn |
| **TỐI ƯU TIẾN HÓA (Buổi 6)** | **Genetic Algorithm (Pop 20, Mut 0.10)** | - | **0.8146** | **Trọng số lớp tối ưu: [1.0, 2.36, 1.87]** | **Hội tụ toàn cục, vượt trội so với ban đầu (0.7980)** |
| **Học máy cổ điển (Buổi 10)**| Logistic Regression | 89.82% | 0.7972 | Rất tốt (Odds Ratio: ASTV 4.75x, LB 4.47x) | Không nắm bắt được quan hệ phi tuyến |
| **Học máy cổ điển** | KNN (k=3, Đã chuẩn hóa) | 91.64% | 0.8408 | Thấp (Khoảng cách Euclidean) | Nhạy cảm với nhiễu; chuẩn hóa tăng <= 0.85 điểm % |
| **Học máy cổ điển** | Cây quyết định (max_depth=6) | 93.73% | 0.8848 | Trực quan (Cây phân nhánh rõ ràng) | Dễ overfitting nếu không giới hạn độ sâu |
| **Học máy cổ điển** | Support Vector Machine (RBF Kernel) | 90.86% | 0.8219 | Hộp đen ranh giới phi tuyến (7-Fold: 90.39%) | Khó giải thích trọng số |
| **Học sâu (Buổi 12)** | Keras MLP (class_weight + EarlyStop) | 89.56% | 0.8450 | Hộp đen (Dừng tại Epoch 53, 3 seeds: 89.99% ± 0.81%) | Bác sĩ khó tin tưởng khi ra quyết định mổ |
| **MÔ HÌNH XUẤT SẮC NHẤT** | **Random Forest Pipeline (200 cây)** | **95.04%** | **0.9043** | **Rất tốt (Gini Imp: ASTV, ALTV, MSTV)** | **Rất thấp: Recall Lớp 3 đạt 90.62% (29/32 ca)** |

---

## 5. CHI TIẾT MA TRẬN NHẦM LẪN MÔ HÌNH RANDOM FOREST TRÊN TẬP TEST (383 MẪU)

```text
               Predicted Normal   Predicted Suspect   Predicted Pathologic
Actual Normal             293                 3                      1      (293/297 = 98.65%)
Actual Suspect             10                42                      2      ( 42/54  = 77.78%)
Actual Pathologic           1                 2                     29      ( 29/32  = 90.62%)
```
* **Tổng thể Test Accuracy:** `95.04%` (364 / 383 mẫu kiểm thử).
* **7-Fold Stratified CV trên Train:** `94.25% ± 1.17%`.
* **Macro-Precision:** `92.12%`, **Macro-Recall:** `89.02%`, **Macro-F1:** `90.43%`.
* **ROC-AUC One-vs-Rest:** `0.9919` (Khả năng phân tách đa lớp ở mức xuất sắc).
* **Chất lượng dự đoán xác suất (Brier Score Loss):** Normal = `0.0278`, Suspect = `0.0338`, Pathologic = `0.0131` -> Mean Brier = `0.0249` (Tiệm cận 0, chất lượng dự đoán xác suất ở mức rất tốt, đáng tin cậy trong thực hành lâm sàng).

---

## 6. MINH HỌA TÍNH TAY NGÀY 7 (CÂU 6 - BUỔI 12)
* **Lưu ý:** Bộ trọng số $W$ và $V$ dưới đây là giả định nhằm mục đích minh họa trực quan phương pháp tính tay 2 tầng theo đề thi tại lớp; dữ liệu đầu vào được lấy chính xác từ Ca bệnh số 1 tập Train.
* **Nguồn dữ liệu:** Lấy chính xác từ ca bệnh số 1 tập Train (Row 0):
  + ASTV đo: `59.0%` -> Chuẩn hóa $x_1 = 0.6894$
  + ALTV đo: `0.0%` -> Chuẩn hóa $x_2 = -0.5429$
  + Nhãn thực tế: $y = 1$ (Normal - index 0 trong 3 lớp).
* **Forward Pass tầng ẩn (ReLU):** $z_1 = 0.0897 	o h_1 = 0.0897$; $z_2 = 0.2836 	o h_2 = 0.2836$.
* **Softmax tầng ra:** $z_{out} = [0.203, 0.2732, 0.2791] 	o P = [0.3173, 0.3403, 0.3424]$.
* **Categorical Cross-Entropy Loss:** $L = -\ln(P[0]) = 1.1480$.
* **Backpropagation:** $\delta_{out} = P - y_{onehot} = [-0.6827, 0.3403, 0.3424]$. Cập nhật trọng số tầng ra $V_{new} = [[0.2061, 0.4969, 0.0969], [0.3194, 0.0903, 0.5903]]$.

---

## 7. HƯỚNG DẪN CÀI ĐẶT VÀ THỰC THI

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
Toàn bộ 12 cells đã được chạy sẵn và lưu đầy đủ kết quả thật 100%.

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

## 8. BẢN QUYỀN VÀ XÁC THỰC BÀI NÀY
* Sinh viên cam kết toàn bộ nội dung trong bài nộp được thực hiện độc lập, nghiêm túc, bám sát từng dòng tham số trong file Excel đề tài của Khoa.
* Các sản phẩm phục vụ bài thi trực tiếp tại lớp:
  + Giấy thi tính tay Ngày 7: Đã chuẩn bị sẵn đề cương tính tay Softmax 3 lớp + Cross-Entropy Loss + Gradient Descent cho mạng nơ-ron MLP với số liệu ca bệnh thật.
  + Vấn đáp & chỉnh sửa code Ngày 7: Nắm vững cấu trúc Pipeline, ColumnTransformer, bộ 10 luật hệ chuyên gia, thuật toán GA tối ưu trọng số lớp, và mô hình Random Forest tối ưu.
