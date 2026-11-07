#!/usr/bin/env python3
"""
University Academic Word Report Builder (.docx).
Generates standardized academic documents adhering to Vietnamese & International university thesis guidelines.
"""

import sys
import os
import argparse
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

PRIMARY_HEX = "1A365D"   # Deep Navy
SECONDARY_HEX = "2B6CB0" # Slate Blue
GRAY_LIGHT_HEX = "F7FAFC"

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_academic_report(output_path: str = "BaoCao_HocThuat_Chuan.docx", title: str = "BÁO CÁO NGHIÊN CỨU KHOA HỌC", student_name: str = "Nguyễn Quách Phú Tài", student_id: str = "123000609"):
    doc = Document()

    # 1. Page Setup: 2.5 cm (approx 1 inch) margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.18) # 3.0 cm for binding
        section.right_margin = Inches(0.8) # 2.0 cm

    # 2. Cover Page
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("TRƯỜNG ĐẠI HỌC ...\nKHOA CÔNG NGHỆ THÔNG TIN\n-----------------------")
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(13)
    r_inst.font.bold = True

    for _ in range(3): doc.add_paragraph()

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_type = p_title.add_run("BÁO CÁO ĐỒ ÁN CUỐI KỲ\n")
    r_type.font.name = "Times New Roman"
    r_type.font.size = Pt(18)
    r_type.font.bold = True
    r_type.font.color.rgb = RGBColor(26, 54, 93)

    r_subj = p_title.add_run(f"{title}\n")
    r_subj.font.name = "Times New Roman"
    r_subj.font.size = Pt(16)
    r_subj.font.bold = True

    for _ in range(5): doc.add_paragraph()

    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_info.paragraph_format.left_indent = Inches(1.5)
    
    r_info = p_info.add_run(
        f"Sinh viên thực hiện : {student_name}\n"
        f"Mã số sinh viên     : {student_id}\n"
        f"Lớp sinh hoạt       : 23CT113\n"
        f"Giảng viên hướng dẫn: Bộ môn Trí tuệ Nhân tạo\n"
    )
    r_info.font.name = "Times New Roman"
    r_info.font.size = Pt(12)

    for _ in range(2): doc.add_paragraph()
    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_date = p_date.add_run("Tháng 11 / 2026")
    r_date.font.name = "Times New Roman"
    r_date.font.size = Pt(12)
    r_date.font.italic = True

    doc.add_page_break()

    # 3. Main Sections Template
    sections_outline = [
        ("1. TỔNG QUAN VÀ ĐẶT VẤN ĐỀ", [
            "1.1. Bối cảnh thực tiễn và tính cấp thiết của đề tài.",
            "1.2. Mục tiêu nghiên cứu và các câu hỏi cần giải quyết.",
            "1.3. Đối tượng và phạm vi nghiên cứu."
        ]),
        ("2. CƠ SỞ DỮ LIỆU VÀ TIỀN XỬ LÝ", [
            "2.1. Nguồn dữ liệu và đặc tả các thuộc tính đo lường.",
            "2.2. Kiểm soát rò rỉ dữ liệu (Data Leakage Prevention).",
            "2.3. Quy trình tiền xử lý bằng ColumnTransformer."
        ]),
        ("3. PHƯƠNG PHÁP NGHIÊN CỨU VÀ MÔ HÌNH HÓA", [
            "3.1. Hệ chuyên gia dựa trên tri thức (Rule-based System).",
            "3.2. Không gian tìm kiếm có thông tin (Greedy & A* Search).",
            "3.3. Tối ưu hóa đặc trưng bằng Giải thuật Di truyền (GA).",
            "3.4. Mô hình học máy phân loại và Mạng nơ-ron (MLP)."
        ]),
        ("4. KẾT QUẢ THỰC NGHIỆM VÀ THẢO LUẬN", [
            "4.1. Bảng đối chiếu hiệu năng giữa các giải pháp.",
            "4.2. Phân tích ma trận nhầm lẫn và sai số lâm sàng.",
            "4.3. Bàn luận về tính khả thi khi ứng dụng thực tế."
        ]),
        ("5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", [
            "5.1. Các đóng góp chính của đề tài.",
            "5.2. Hạn chế hiện tại của mô hình.",
            "5.3. Định hướng mở rộng trong tương lai."
        ])
    ]

    for sec_title, subsections in sections_outline:
        h1 = doc.add_heading(sec_title, level=1)
        h1_run = h1.runs[0]
        h1_run.font.name = "Times New Roman"
        h1_run.font.color.rgb = RGBColor(26, 54, 93)
        h1_run.font.bold = True
        
        p = doc.add_paragraph("Nội dung chi tiết được trình bày tại đây...")
        p.paragraph_format.line_spacing = 1.25
        p.runs[0].font.name = "Times New Roman"

        for sub in subsections:
            h2 = doc.add_heading(sub, level=2)
            h2_run = h2.runs[0]
            h2_run.font.name = "Times New Roman"
            h2_run.font.color.rgb = RGBColor(43, 108, 176)
            
            p_sub = doc.add_paragraph("Trình bày nội dung chi tiết của tiểu mục...")
            p_sub.runs[0].font.name = "Times New Roman"

    # Add Sample Academic Table
    doc.add_paragraph()
    p_tbl_cap = doc.add_paragraph("Bảng 1: Bảng so sánh các chỉ số hiệu năng trên tập kiểm tra")
    p_tbl_cap.runs[0].font.name = "Times New Roman"
    p_tbl_cap.runs[0].font.bold = True
    p_tbl_cap.runs[0].font.italic = True

    table = doc.add_table(rows=4, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Mô hình", "Test Accuracy", "Macro F1-score", "Ghi chú"]
    rows_data = [
        ["Hệ chuyên gia (10 Luật)", "82.25%", "0.7410", "Suy diễn tiến & lùi"],
        ["Mạng nơ-ron (MLP)", "88.51%", "0.8240", "Hội tụ sau 42 epochs"],
        ["Random Forest (Tốt nhất)", "95.04%", "0.9015", "Đóng gói BestModel.joblib"]
    ]

    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.text = h
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, PRIMARY_HEX)
        set_cell_margins(cell, 120, 120, 150, 150)

    for r_idx, row in enumerate(rows_data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.paragraphs[0]
            if c_idx in [1, 2]: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_cell_margins(cell, 100, 100, 120, 120)
            if r_idx % 2 == 1: set_cell_background(cell, GRAY_LIGHT_HEX)

    doc.save(output_path)
    print(f"[+] Successfully generated Academic Word Report: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create standardized academic Word report.")
    parser.add_argument("--output", default="BaoCao_HocThuat_Chuan.docx")
    parser.add_argument("--title", default="ĐÁNH GIÁ SỨC KHỎE THAI NHI TỪ BIỂU ĐỒ TIM THAI")
    args = parser.parse_args()
    create_academic_report(args.output, args.title)
