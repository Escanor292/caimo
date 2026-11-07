# Academic Humanizer & Anti-AI Detection Rules
## Cẩm nang Tối ưu Văn phong Học thuật & Xóa Dấu vết AI (Turnitin, GPTZero, Desklib)
### Tích hợp tinh hoa từ DIPPER, Proselint, Write-Good, Parrot & GPT_Academic

Tài liệu này tổng hợp các kỹ thuật cơ học, từ vựng và cấu trúc ngữ pháp học thuật rút ra từ các nghiên cứu và công cụ mã nguồn mở hàng đầu thế giới (DIPPER - AllenAI, Proselint, write-good, Parrot Paraphraser, GPT_Academic, Fabric).

---

## I. BA NGUYÊN TẮC PARAPHRASE HỌC THUẬT (THE PARROT TRIAD)

Khi viết lại câu văn để xóa dấu vết máy viết, luôn đảm bảo cân bằng 3 trục của **Parrot Paraphraser**:
1. **Adequacy (Bảo toàn ý nghĩa):** Tuyệt đối không thay đổi sự thật khoa học, số liệu thực nghiệm hoặc kết luận cốt lõi.
2. **Fluency (Trôi chảy ngữ pháp):** Câu từ tự nhiên, mạch lạc, không dùng từ điển đồng nghĩa một cách gượng ép (tránh "thesaurus replacement" thô thiển).
3. **Diversity (Độ sai khác cấu trúc):** Thay đổi căn bản hình thái ngữ pháp (đổi thể chủ động/bị động, tách câu, gộp câu, đảo trật tự mệnh đề).

---

## II. KỸ THUẬT DIPPER (DISCOURSE PARAPHRASING)

Nghiên cứu của AllenAI & UMass (Krishna et al.) chứng minh rằng việc chỉ thay thế từ vựng đơn lẻ vẫn bị các bộ phân loại RoBERTa/DeBERTa bắt được. Muốn phá vỡ mô hình phân loại, ta phải kiểm soát 2 thông số:

### 1. Lexical Diversity (Độ biến thiên từ vựng):
* Thay thế các từ vựng mang tính khái quát cao bằng các thuật ngữ định danh hẹp và chính xác hơn.
* Thay vì viết: *"Mô hình phân loại dữ liệu rất tốt"* $\rightarrow$ Viết: *"Thuật toán Random Forest hội tụ nhanh trên 21 thuộc tính đo lường tim thai"*.

### 2. Order Diversity (Đảo trật tự mệnh đề & liên kết diễn ngôn):
* **Đảo mệnh đề phụ lên đầu câu (Fronted Dependent Clauses):**
  * *Bản AI gốc:* *"Random Forest đạt kết quả tốt nhất vì nó có khả năng xử lý các thuộc tính phi tuyến tính hiệu quả."*
  * *Bản DIPPER đảo:* *"Nhờ năng lực phân tách các thuộc tính phi tuyến tính phức tạp, Random Forest vượt trội hoàn toàn so với mô hình hồi quy tuyến tính cổ điển."*
* **Tách câu ghép thành cặp câu ngắn - dài tương phản:**
  * *Bản AI gốc:* *"Mô hình có độ chính xác 95% nhưng vẫn còn nhầm lẫn giữa lớp 2 và lớp 3 do sự chồng lấn phân phối của chỉ số ASTV."*
  * *Bản DIPPER tái cấu trúc:* *"Mô hình đạt độ chính xác 95%. Tuy vậy, hiện tượng chồng lấn chỉ số ASTV tại các ngưỡng cận biên vẫn dẫn đến sai lệch đáng kể giữa nhóm nghi ngờ và nhóm bệnh lý thực sự."*

---

## III. BỘ QUY TẮC PROSELINT & WRITE-GOOD (CHỮA BỆNH VĂN PHONG AI)

### 1. Triệt tiêu "Bệnh danh từ hóa" (Nominalization / Zombie Nouns)
AI rất thích biến các động từ mạnh thành các cụm danh từ cồng kềnh, làm câu văn chết lặng và mang đậm "mùi máy":

| Cụm danh từ AI rườm rà (CẤM) | Động từ hành động của con người |
| :--- | :--- |
| *tiến hành thực hiện việc phân tích* | **phân tích** |
| *đưa ra kết luận khẳng định* | **kết luận** |
| *tiến hành quá trình tối ưu hóa* | **tối ưu hóa** |
| *make an examination of* | **examine / analyze** |
| *conduct an investigation into* | **investigate** |
| *perform a demonstration of* | **demonstrate / show** |
| *take into consideration* | **consider** |

### 2. Cắt bỏ "Từ thoái thác & Hư từ đệm" (Weasel Words & Padding)
Các từ thừa thãi khiến câu văn dài dòng mà không đem lại giá trị học thuật:
* **Tiếng Việt cần loại bỏ:** *rất, vô cùng, cực kỳ, tương đối, nhìn chung thì, trên thực tế thì, rõ ràng là, hiển nhiên là, có thể nói rằng*.
* **Tiếng Anh cần loại bỏ:** *extremely, fairly, remarkably, quite, clearly, obviously, virtually, essentially, in a sense, in terms of, it goes without saying that*.

### 3. Kiểm soát "Thể bị động quá mức" (Excessive Passive Voice)
* AI thường lạm dụng câu bị động để nghe có vẻ khách quan (*"It was observed that..."*, *"Việc xử lý dữ liệu được thực hiện bởi..."*).
* **Quy tắc:** Giữ tỷ lệ câu bị động dưới **25%**. Dùng thể chủ động có danh xưng học thuật tự nhiên (*"Chúng tôi áp dụng mô hình..."*, *"Thực nghiệm chứng minh rằng..."*).

---

## IV. BẢNG TỪ VỰNG BỊ CẤM TOÀN DIỆN (COMPREHENSIVE BANNED LIST)

### 1. Tiếng Việt (Cấm 100% khi viết học thuật)
* **Cụm mở bài sáo rỗng:** *"Trong bối cảnh hiện nay / kỷ nguyên số 4.0...", "Không thể phủ nhận rằng...", "Như chúng ta đã biết...", "Từ xa xưa đến nay...", "Tóm lại, việc..."*.
* **Cụm ca ngợi sáo rỗng:** *"Đóng vai trò vô cùng quan trọng / then chốt / không thể thiếu...", "Là một bước tiến mang tính đột phá...", "Mở ra một chương mới..."*.
* **Cụm liệt kê đối xứng:** 3 gạch đầu dòng có cấu trúc ngữ pháp và độ dài y hệt nhau.

### 2. Tiếng Anh (Cấm 100% - Tránh gắn cờ Turnitin / GPTZero)
* **Verbs:** *delve, underscore, foster, harness, embark, bolster, resonate, navigate, elucidate*.
* **Nouns & Adjectives:** *tapestry, testament, pivotal, intricate, crucial, paramount, beacon, realm, multifaceted, myriad, unprecedented, quintessential*.
* **Transitions:** *Furthermore, Moreover, In conclusion, It is important to note that, A double-edged sword, In today's fast-paced world*.

---

## V. CÁC SYSTEM PROMPTS MẪU TỪ FABRIC & GPT_ACADEMIC

Khi hướng dẫn AI viết bài, sử dụng các chỉ thị sau để khóa chặt văn phong:

```text
[Direct Academic Persona]
You are a rigorous, senior peer reviewer and academic researcher. 
Write with intellectual density, surgical precision, and natural syntactic variance:
- Never use generic introductory throat-clearing ("In this modern era...", "It is important to remember...").
- Alternate cadence using a 3-tier structure: short assertive claims (4-8 words), dense analytical arguments (28-40 words with semicolons/dashes), and empirical observations (12-18 words).
- Eliminate nominalizations: use direct, active transitive verbs.
- Ground all arguments in concrete parameters, quantitative thresholds, or trade-off analysis.
```
