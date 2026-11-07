# Academic Humanizer & Anti-AI Detection Rules
## Quy tắc Viết & Chuốt Văn phong Học thuật Tránh Máy quét AI (Turnitin, GPTZero, Desklib)

Tài liệu này tổng hợp toàn bộ các nguyên tắc cơ học, từ vựng và cấu trúc ngữ pháp giúp văn bản học thuật (báo cáo, tiểu luận, luận văn, nghiên cứu) giữ vững tính trang trọng nhưng mang dấu ấn tư duy con người, triệt tiêu các đặc trưng thống kê mà các bộ quét AI (Turnitin AI Detection, GPTZero, Desklib DeBERTa, CopyLeaks) sử dụng để gắn cờ.

---

## I. CƠ CHẾ BẮT BÀI CỦA CÁC BỘ QUÉT AI

Các bộ quét AI không "hiểu" nội dung; chúng đo lường **3 chỉ số thống kê xác suất**:

1. **Perplexity (Độ ngạc nhiên của từ vựng):**
   * *AI:* Luôn chọn từ có xác suất xuất hiện cao nhất tiếp theo trong ngữ cảnh (đường đi an toàn, dễ đoán).
   * *Người thật:* Dùng từ vựng chuyên ngành chính xác, các động từ hành động cụ thể, thỉnh thoảng dùng quán ngữ tự nhiên hoặc cách diễn đạt phi tuyến tính.
2. **Burstiness (Độ biến thiên nhịp điệu / chiều dài câu):**
   * *AI:* Các câu có chiều dài rất đồng đều (trung bình 15–22 từ/câu, độ lệch chuẩn rất thấp, $\text{Burstiness} < 0.35$).
   * *Người thật:* Nhịp điệu lúc dồn dập, lúc trầm lắng (câu 5 từ xen kẽ câu phức 35 từ có mệnh đề phụ, $\text{Burstiness} > 0.45$).
3. **Tính đối xứng và cấu trúc đoạn rập khuôn:**
   * *AI:* Mỗi đoạn luôn đúng 3–4 câu: 1 câu chủ đề $\rightarrow$ 2 câu giải thích $\rightarrow$ 1 câu tóm tắt/triết lý; các gạch đầu dòng luôn có độ dài tương đương nhau.

---

## II. DANH SÁCH TỪ VỰNG VÀ CẤU TRÚC BỊ CẤM TUYỆT ĐỐI (RED FLAGS)

### 1. Tiếng Việt (Bắt buộc loại bỏ 100%)

| Mẫu câu AI rập khuôn (CẤM) | Cách người thật diễn đạt thay thế |
| :--- | :--- |
| *"Trong bối cảnh hiện nay / Trong kỷ nguyên số 4.0..."* | Vào thẳng vấn đề: *"Khi khối lượng hồ sơ bệnh án số hóa tăng nhanh..."* |
| *"Không thể phủ nhận rằng..."* | *"Thực nghiệm cho thấy..."* hoặc đưa số liệu trực tiếp. |
| *"Đóng vai trò vô cùng quan trọng / then chốt / không thể thiếu..."* | Nêu rõ tác dụng cụ thể: *"Giúp rút ngắn 40% thời gian hội chẩn..."* |
| *"Như chúng ta đã biết..."* | Bỏ hẳn cụm này, bắt đầu trực tiếp bằng luận điểm. |
| *"Tóm lại, việc... là một bước tiến mang tính đột phá..."* | Nêu kết luận định lượng: *"Kết quả trên khẳng định mô hình đủ độ tin cậy để..."* |
| *"Mặt khác,... Bên cạnh đó,... Hơn nữa,..."* (đầu mỗi câu) | Thay bằng liên kết ngữ nghĩa: *"Tuy nhiên,", "Đáng lưu ý là,", "Ngược lại,"*. |
| 3 gạch đầu dòng có cấu trúc ngữ pháp và độ dài y hệt nhau | Viết thành đoạn văn liên tục hoặc để độ dài các ý tự nhiên theo độ phức tạp. |

### 2. Tiếng Anh (Bắt buộc loại bỏ 100%)

| AI Red-Flag Words & Phrases (BANNED) | Human Academic Alternatives |
| :--- | :--- |
| **delve / delve into** | investigate, examine, inspect, analyze, assess |
| **tapestry / rich tapestry** | complex framework, system, interplay, domain |
| **testament / stands as a testament** | evidence, demonstration, indicates, confirms |
| **underscore / underline** | emphasize, highlight, show, reveal |
| **pivotal / crucial / paramount** | critical, key, necessary, fundamental, significant |
| **intricate / nuances** | detailed, specific mechanisms, complexities |
| **foster / harness / embark** | promote, develop, apply, initiate, employ |
| **furthermore / moreover** (used repeatedly) | additionally, in turn, consequently, notably, however |
| **beacon / realm / overarching** | benchmark, field, context, general, primary |
| **"In today's fast-paced world..."** | Directly cite the problem: *"Modern clinical settings require..."* |
| **"It is important to remember that..."** | Cut the fluff: *"Note that..."* or state the fact directly. |
| **"A double-edged sword"** | State the specific trade-off: *"While accuracy improves, latency increases by 15%."* |

---

## III. KỸ THUẬT NÂNG CAO BURSTINESS (TRỘN NHỊP CÂU)

Để vượt qua các thuật toán đo độ cong xác suất (Fast-DetectGPT, GPTZero), bài viết **bắt buộc phải tuân thủ quy tắc 3 tầng nhịp điệu (3-Tier Length Pattern)**:

1. **Tầng 1 - Câu ngắn dứt khoát (Punchy Short: 4–9 từ):**
   * Dùng để chốt luận điểm, nêu câu hỏi hoặc tạo điểm nhấn.
   * *Ví dụ:* *"Sai số này là không thể chấp nhận."* hoặc *"The baseline model failed."*
2. **Tầng 2 - Câu phức phân tích sâu (Compound / Complex: 28–42 từ):**
   * Chứa mệnh đề phụ, quan hệ nhân quả, điều kiện ràng buộc hoặc dấu chấm phẩy (`;`).
   * *Ví dụ:* *"Mặc dù Random Forest đạt độ chính xác 95% trên tập kiểm tra, việc thiếu hụt dữ liệu ở nhóm bệnh lý nhóm 3 khiến độ nhạy giảm rõ rệt; điều này đòi hỏi các bác sĩ lâm sàng phải can thiệp trực tiếp thay vì chỉ dựa vào dự đoán tự động."*
3. **Tầng 3 - Câu chức năng thông thường (Moderate: 12–18 từ):**
   * Dẫn dắt thông tin hoặc trình bày phương pháp thực nghiệm.

> **Quy tắc vàng:** Không bao giờ để 3 câu liên tiếp có số lượng từ xấp xỉ nhau (chênh lệch dưới 4 từ).

---

## IV. NÂNG CAO TÍNH HỌC THUẬT (AUTHENTIC ACADEMIC STANCE)

1. **Tính cụ thể hóa (Specific Grounding):** Thay thế mọi tính từ chung chung bằng số liệu hoặc tên định danh thực tế (tên biến, ngưỡng đo, chỉ số phần trăm).
2. **Thái độ phản biện (Critical Hedging):** Người viết nghiên cứu thật luôn chỉ ra giới hạn của phương pháp:
   * Tránh tuyệt đối: *"Phương pháp này hoàn hảo và giải quyết triệt để vấn đề."* (Giọng điệu AI)
   * Viết chuẩn: *"Mặc dù kết quả cho thấy mức cải thiện 3.2% F1-score, phương pháp vẫn còn nhạy cảm với nhiễu tại các phân vị cực trị."* (Giọng điệu học giả)
3. **Đa dạng hóa dấu câu:** Tự nhiên sử dụng dấu gạch ngang giải thích (`—`), dấu ngoặc đơn chú thích `(...)`, dấu hai chấm `:` và dấu chấm phẩy `;`.
