# app.py - Ứng dụng Web Streamlit hỗ trợ chẩn đoán sức khỏe thai nhi từ biểu đồ tim thai (DT69)
# Phần nâng cao cộng điểm (Câu 8): Triển khai ứng dụng Gradio/Streamlit có giải thích kết quả
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Cấu hình trang web
st.set_page_config(
    page_title="Chẩn Đoán Sức Khỏe Thai Nhi CTG - DT69",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header trang web
st.title("👶 HỆ THỐNG HỖ TRỢ CHẨN ĐOÁN LÂM SÀNG TIM THAI (CLINICAL DSS)")
st.markdown("""
**Đồ án môn:** Nhập môn Trí tuệ Nhân tạo — **Đề tài DT69:** Đánh giá sức khỏe thai nhi từ biểu đồ tim thai (*Cardiotocography - UCI ID 193*)  
**Sinh viên thực hiện:** Nguyễn Quách Phú Tài — **MSSV:** 123000609 — **Lớp:** 23CT113
""")
st.divider()

# Nạp mô hình pipeline đã đóng gói
MODEL_PATH = 'DT69_123000609_BestModel.joblib'
if os.path.exists(MODEL_PATH):
    pipeline = joblib.load(MODEL_PATH)
    st.sidebar.success("✓ Đã nạp thành công mô hình: `DT69_123000609_BestModel.joblib`")
else:
    st.sidebar.error("Không tìm thấy file mô hình `DT69_123000609_BestModel.joblib`!")
    st.stop()

# Cơ sở tri thức 10 luật IF-THEN sản khoa
RULES = [
    {'id': 'R1', 'if': ['DP_cao'], 'then': 'Bệnh lý (Pathologic)', 'desc': 'Nhịp giảm kéo dài (DP > 0) -> Cảnh báo Bệnh lý'},
    {'id': 'R2', 'if': ['DL_cao', 'ASTV_cao'], 'then': 'Nguy cơ thiếu oxy', 'desc': 'Nhịp giảm muộn kèm dao động ngắn hạn bất thường cao'},
    {'id': 'R3', 'if': ['Nguy cơ thiếu oxy', 'Khong_co_AC'], 'then': 'Bệnh lý (Pathologic)', 'desc': 'Thiếu oxy và không có nhịp tăng -> Cảnh báo Bệnh lý'},
    {'id': 'R4', 'if': ['LB_cham_nang', 'MSTV_thap'], 'then': 'Bệnh lý (Pathologic)', 'desc': 'Nhịp tim cơ bản chậm (<110) kèm dao động ngắn hạn thấp'},
    {'id': 'R5', 'if': ['LB_nhanh', 'Khong_co_AC'], 'then': 'Đa nhịp tim nghi ngờ', 'desc': 'Nhịp tim cơ bản nhanh (>160) và không có nhịp tăng'},
    {'id': 'R6', 'if': ['Đa nhịp tim nghi ngờ'], 'then': 'Nghi ngờ (Suspect)', 'desc': 'Dấu hiệu nhịp nhanh thiếu đáp ứng -> Nghi ngờ'},
    {'id': 'R7', 'if': ['ASTV_cao', 'ALTV_cao'], 'then': 'Dao động kém', 'desc': 'Cả ASTV và ALTV đều vượt ngưỡng cảnh báo (Q75)'},
    {'id': 'R8', 'if': ['Dao động kém', 'Khong_co_AC'], 'then': 'Nghi ngờ (Suspect)', 'desc': 'Dao động kém và không có nhịp tăng -> Nghi ngờ'},
    {'id': 'R9', 'if': ['LB_binh_thuong', 'Co_AC', 'Khong_co_DP'], 'then': 'Tín hiệu tốt', 'desc': 'Nhịp cơ bản ổn định, có nhịp tăng, không có DP'},
    {'id': 'R10', 'if': ['Tín hiệu tốt'], 'then': 'Bình thường (Normal)', 'desc': 'Tín hiệu tim thai đáp ứng tốt -> Bình thường'}
]

def expert_system_eval(row):
    facts = set()
    if row['DP'] > 0: facts.add('DP_cao')
    else: facts.add('Khong_co_DP')
    if row['DL'] > 0: facts.add('DL_cao')
    if row['ASTV'] > 61.0: facts.add('ASTV_cao')
    if row['ALTV'] > 12.0: facts.add('ALTV_cao')
    if row['MSTV'] < 0.70: facts.add('MSTV_thap')
    if row['AC'] == 0: facts.add('Khong_co_AC')
    else: facts.add('Co_AC')
    if row['LB'] < 110: facts.add('LB_cham_nang')
    elif row['LB'] > 160: facts.add('LB_nhanh')
    else: facts.add('LB_binh_thuong')
    
    fired = []
    changed = True
    while changed:
        changed = False
        for r in RULES:
            if r['then'] not in facts and all(c in facts for c in r['if']):
                facts.add(r['then'])
                fired.append(f"**{r['id']}:** {r['desc']}")
                changed = True
                
    if 'Bệnh lý (Pathologic)' in facts: pred = "Bệnh lý (Lớp 3)"
    elif 'Nghi ngờ (Suspect)' in facts: pred = "Nghi ngờ (Lớp 2)"
    else: pred = "Bình thường (Lớp 1)"
    return pred, fired

# Sidebar: Chọn mẫu sẵn hoặc tự chỉnh
st.sidebar.header("📋 LỰA CHỌN CA LÂM SÀNG")
sample_choice = st.sidebar.selectbox(
    "Chọn một ca bệnh nhân mẫu từ tập dữ liệu kiểm thử:",
    [
        "Tự điều chỉnh thủ công (Sliders)",
        "Ca 1: Thai nhi khỏe mạnh (Normal - Lớp 1)",
        "Ca 2: Thai nhi nghi ngờ bất thường (Suspect - Lớp 2)",
        "Ca 3: Suy tim thai cấp tính (Pathologic - Lớp 3)"
    ]
)

# Giá trị mặc định theo ca mẫu
if sample_choice == "Ca 1: Thai nhi khỏe mạnh (Normal - Lớp 1)":
    def_vals = {'LB': 132, 'AC': 0.006, 'FM': 0.0, 'UC': 0.006, 'DL': 0.003, 'DS': 0.0, 'DP': 0.0,
                'ASTV': 17.0, 'MSTV': 2.1, 'ALTV': 0.0, 'MLTV': 10.4, 'Width': 130, 'Min': 68, 'Max': 198,
                'Nmax': 6, 'Nzeros': 1, 'Mode': 141, 'Mean': 136, 'Median': 140, 'Variance': 12, 'Tendency': 0}
elif sample_choice == "Ca 2: Thai nhi nghi ngờ bất thường (Suspect - Lớp 2)":
    def_vals = {'LB': 120, 'AC': 0.0, 'FM': 0.0, 'UC': 0.0, 'DL': 0.0, 'DS': 0.0, 'DP': 0.0,
                'ASTV': 73.0, 'MSTV': 0.5, 'ALTV': 43.0, 'MLTV': 2.4, 'Width': 64, 'Min': 62, 'Max': 126,
                'Nmax': 2, 'Nzeros': 0, 'Mode': 120, 'Mean': 137, 'Median': 121, 'Variance': 73, 'Tendency': 1}
elif sample_choice == "Ca 3: Suy tim thai cấp tính (Pathologic - Lớp 3)":
    def_vals = {'LB': 134, 'AC': 0.001, 'FM': 0.0, 'UC': 0.010, 'DL': 0.009, 'DS': 0.0, 'DP': 0.002,
                'ASTV': 26.0, 'MSTV': 5.9, 'ALTV': 0.0, 'MLTV': 0.0, 'Width': 150, 'Min': 50, 'Max': 200,
                'Nmax': 5, 'Nzeros': 3, 'Mode': 76, 'Mean': 107, 'Median': 107, 'Variance': 170, 'Tendency': 0}
else:
    def_vals = {'LB': 133, 'AC': 0.003, 'FM': 0.005, 'UC': 0.004, 'DL': 0.002, 'DS': 0.0, 'DP': 0.0,
                'ASTV': 45.0, 'MSTV': 1.3, 'ALTV': 10.0, 'MLTV': 8.0, 'Width': 70, 'Min': 90, 'Max': 160,
                'Nmax': 4, 'Nzeros': 0, 'Mode': 137, 'Mean': 134, 'Median': 138, 'Variance': 18, 'Tendency': 0}

st.subheader("1. Thông số biểu đồ tim thai (CTG Input Features)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("##### Nhịp tim cơ bản & Vận động")
    lb = st.number_input("LB: Nhịp cơ bản (bpm)", min_value=90, max_value=190, value=int(def_vals['LB']), step=1)
    ac = st.number_input("AC: Nhịp tăng/giây", min_value=0.0, max_value=0.02, value=float(def_vals['AC']), step=0.001, format="%.3f")
    fm = st.number_input("FM: Cử động thai/giây", min_value=0.0, max_value=0.5, value=float(def_vals['FM']), step=0.005, format="%.3f")
    uc = st.number_input("UC: Cơn co tử cung/giây", min_value=0.0, max_value=0.02, value=float(def_vals['UC']), step=0.001, format="%.3f")

with col2:
    st.markdown("##### Nhịp giảm (Decelerations)")
    dl = st.number_input("DL: Nhịp giảm nhẹ/giây", min_value=0.0, max_value=0.02, value=float(def_vals['DL']), step=0.001, format="%.3f")
    ds = st.number_input("DS: Nhịp giảm nặng/giây", min_value=0.0, max_value=0.005, value=float(def_vals['DS']), step=0.0001, format="%.4f")
    dp = st.number_input("DP: Nhịp giảm kéo dài/giây", min_value=0.0, max_value=0.01, value=float(def_vals['DP']), step=0.001, format="%.3f")

with col3:
    st.markdown("##### Độ dao động (Variability)")
    astv = st.number_input("ASTV: % dao động ngắn xấu", min_value=10.0, max_value=90.0, value=float(def_vals['ASTV']), step=1.0)
    mstv = st.number_input("MSTV: Dao động ngắn TB", min_value=0.1, max_value=10.0, value=float(def_vals['MSTV']), step=0.1)
    altv = st.number_input("ALTV: % dao động dài xấu", min_value=0.0, max_value=95.0, value=float(def_vals['ALTV']), step=1.0)
    mltv = st.number_input("MLTV: Dao động dài TB", min_value=0.0, max_value=60.0, value=float(def_vals['MLTV']), step=0.5)

with col4:
    st.markdown("##### Phân bố đồ thị (Histogram)")
    width = st.number_input("Width: Độ rộng dải nhịp", min_value=0, max_value=200, value=int(def_vals['Width']), step=1)
    min_val = st.number_input("Min: Nhịp thấp nhất", min_value=40, max_value=160, value=int(def_vals['Min']), step=1)
    max_val = st.number_input("Max: Nhịp cao nhất", min_value=120, max_value=250, value=int(def_vals['Max']), step=1)
    mean_val = st.number_input("Mean: Nhịp trung bình", min_value=60, max_value=190, value=int(def_vals['Mean']), step=1)
    mode_val = st.number_input("Mode: Mốt của nhịp", min_value=60, max_value=190, value=int(def_vals['Mode']), step=1)
    median_val = st.number_input("Median: Trung vị nhịp", min_value=60, max_value=190, value=int(def_vals['Median']), step=1)
    variance_val = st.number_input("Variance: Phương sai nhịp", min_value=0, max_value=300, value=int(def_vals['Variance']), step=1)
    tendency_val = st.selectbox("Tendency: Xu hướng phân bố", options=[-1, 0, 1], index=int(def_vals['Tendency'] + 1))
    nmax_val = int(def_vals['Nmax'])
    nzeros_val = int(def_vals['Nzeros'])

# Gom thành từ điển mẫu dữ liệu
input_data = {
    'LB': lb, 'AC': ac, 'FM': fm, 'UC': uc, 'DL': dl, 'DS': ds, 'DP': dp,
    'ASTV': astv, 'MSTV': mstv, 'ALTV': altv, 'MLTV': mltv, 'Width': width,
    'Min': min_val, 'Max': max_val, 'Nmax': nmax_val, 'Nzeros': nzeros_val,
    'Mode': mode_val, 'Mean': mean_val, 'Median': median_val, 'Variance': variance_val,
    'Tendency': tendency_val
}

st.divider()

# Nút thực hiện chẩn đoán
if st.button("🩺 THỰC HIỆN PHÂN TÍCH & CHẨN ĐOÁN LÂM SÀNG", type="primary", use_container_width=True):
    df_in = pd.DataFrame([input_data])
    
    # 1. Dự đoán qua Random Forest Pipeline
    pred_code = pipeline.predict(df_in)[0]
    pred_proba = pipeline.predict_proba(df_in)[0]
    
    # 2. Đánh giá qua Hệ chuyên gia luật IF-THEN
    expert_pred, expert_fired = expert_system_eval(input_data)
    
    st.subheader("2. Kết quả Chẩn đoán & Đánh giá Rủi ro")
    res_col1, res_col2 = st.columns([1, 1])
    
    with res_col1:
        st.markdown("#### Mô hình Học máy (Random Forest Pipeline)")
        if pred_code == 1:
            st.success(f"### 🟢 BÌNH THƯỜNG (NORMAL)\n**Độ tin cậy:** {pred_proba[0]*100:.2f}%\n\n*Khuyến nghị:* Thai nhi phản ứng tốt. Cho sản phụ theo dõi thai kỳ định kỳ.")
        elif pred_code == 2:
            st.warning(f"### 🟡 NGHI NGỜ BẤT THƯỜNG (SUSPECT)\n**Độ tin cậy:** {pred_proba[1]*100:.2f}%\n\n*Khuyến nghị:* Dao động tim thai kém hoặc nhịp nhanh. Chỉ định đo lại CTG trong 30 phút và siêu âm Doppler rốn.")
        else:
            st.error(f"### 🔴 BÁO ĐỘNG ĐỎ: SUY THAI CẤP TÍNH (PATHOLOGIC)\n**Độ tin cậy:** {pred_proba[2]*100:.2f}%\n\n*Khuyến nghị:* Thai nhi có dấu hiệu thiếu oxy não nghiêm trọng. Cần kích hoạt quy trình hội chẩn mổ lấy thai cấp cứu!")
            
        # Biểu đồ phân phối xác suất bằng Matplotlib (Thuần túy, 100% không phụ thuộc pyarrow)
        import matplotlib.pyplot as plt
        fig_prob, ax_prob = plt.subplots(figsize=(6, 2.5), dpi=150)
        classes = ['Bình thường (1)', 'Nghi ngờ (2)', 'Bệnh lý (3)']
        probs_pct = [pred_proba[0]*100, pred_proba[1]*100, pred_proba[2]*100]
        colors = ['#2ca02c', '#ff7f0e', '#d62728']
        bars = ax_prob.barh(classes, probs_pct, color=colors, height=0.55, edgecolor='black', linewidth=0.5)
        for b, v in zip(bars, probs_pct):
            ax_prob.text(v + 1.5, b.get_y() + b.get_height()/2, f'{v:.2f}%', va='center', fontsize=9, fontweight='bold')
        ax_prob.set_xlim(0, 115)
        ax_prob.set_xlabel('Xác suất dự đoán (%)', fontsize=9)
        ax_prob.grid(True, linestyle='--', alpha=0.5, axis='x')
        plt.tight_layout()
        st.pyplot(fig_prob)
        plt.close(fig_prob)

    with res_col2:
        st.markdown("#### Đối chiếu với Hệ Chuyên Gia Luật (Hybrid AI)")
        st.info(f"**Kết luận Hệ luật:** {expert_pred}")
        st.markdown("**Các luật lâm sàng được kích hoạt:**")
        if expert_fired:
            for r in expert_fired:
                st.markdown(f"- {r}")
        else:
            st.markdown("- *Không có luật cảnh báo bất thường nào được kích hoạt.*")
            
        st.markdown("---")
        st.markdown("#### Giải thích Y khoa (Explainability):")
        explanations = []
        if dp > 0: explanations.append("⚠️ **Xuất hiện nhịp giảm kéo dài (DP > 0):** Dấu hiệu suy thai cấp tính nghiêm trọng nhất do chèn ép rốn.")
        if astv > 61.0: explanations.append(f"⚠️ **ASTV ({astv:.1f}%) vượt ngưỡng phân vị 75%:** Rối loạn điều hòa thần kinh tim thai.")
        if altv > 12.0: explanations.append(f"⚠️ **ALTV ({altv:.1f}%) vượt ngưỡng phân vị 75%:** Dao động dài hạn bị triệt tiêu.")
        if ac == 0: explanations.append("⚠️ **Mất hoàn toàn nhịp tăng (AC = 0):** Thai nhi không có đáp ứng cử động.")
        if lb < 110: explanations.append(f"⚠️ **Nhịp cơ bản chậm nghiêm trọng ({lb} bpm):** Dấu hiệu ức chế cơ tim thai nhi.")
        if variance_val > 100: explanations.append(f"⚠️ **Phương sai nhịp tim rất lớn ({variance_val}):** Loạn nhịp tim thai.")
        
        if explanations:
            for ex in explanations: st.markdown(ex)
        else:
            st.markdown("✓ Tất cả các chỉ số nhịp tim, nhịp tăng và dao động đều nằm trong ngưỡng sinh lý an toàn.")

