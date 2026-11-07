#!/usr/bin/env python3
"""
Academic Slide Deck Builder (.pptx).
Generates standardized 16:9 widescreen academic presentations with structured layouts.
"""

import sys
import os
import argparse
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Professional Academic Palette
COLOR_NAVY = RGBColor(24, 43, 73)
COLOR_BLUE = RGBColor(43, 108, 176)
COLOR_GRAY_BG = RGBColor(248, 249, 250)
COLOR_TEXT_DARK = RGBColor(40, 40, 40)
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_BORDER = RGBColor(226, 232, 240)

def create_slide_deck(output_path: str = "Slide_ThuyetTrinh_Chuan.pptx", title: str = "ĐÁNH GIÁ SỨC KHỎE THAI NHI TỪ BIỂU ĐỒ TIM THAI", student_name: str = "Nguyễn Quách Phú Tài", student_id: str = "123000609"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text=""):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        if category_text:
            p_cat = tf.paragraphs[0]
            p_cat.text = category_text.upper()
            p_cat.font.size = Pt(11)
            p_cat.font.bold = True
            p_cat.font.color.rgb = COLOR_BLUE
            p_title = tf.add_paragraph()
        else:
            p_title = tf.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_NAVY

    # SLIDE 1: Title Slide
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_NAVY
    bg1.line.color.rgb = COLOR_NAVY

    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(3.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p_topic = tf1.paragraphs[0]
    p_topic.text = "BÁO CÁO ĐỒ ÁN CUỐI KỲ - NHẬP MÔN AI"
    p_topic.font.size = Pt(14)
    p_topic.font.bold = True
    p_topic.font.color.rgb = RGBColor(99, 179, 237)

    p_main = tf1.add_paragraph()
    p_main.text = title
    p_main.font.size = Pt(32)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_WHITE

    p_meta = tf1.add_paragraph()
    p_meta.text = f"\nSinh viên: {student_name} | MSSV: {student_id} | Lớp: 23CT113"
    p_meta.font.size = Pt(16)
    p_meta.font.color.rgb = RGBColor(226, 232, 240)

    # SLIDE 2: Agenda
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Nội Dung Báo Cáo", "LỘ TRÌNH TRÌNH BÀY")
    agenda_items = [
        ("01", "Đặt vấn đề & Mục tiêu", "Bối cảnh thực tiễn và chỉ số thành công"),
        ("02", "Phương pháp & Kỹ thuật", "Hệ chuyên gia, Tìm kiếm A*, GA & Machine Learning"),
        ("03", "Kết quả thực nghiệm", "Bảng đối chiếu hiệu năng và ma trận nhầm lẫn"),
        ("04", "Thảo luận & Phân tích lỗi", "Lý giải ca bất đồng và rủi ro triển khai"),
        ("05", "Đề xuất & Ứng dụng Web", "3 hướng phát triển và demo Streamlit")
    ]
    for i, (num, h, sub) in enumerate(agenda_items):
        y_pos = Inches(1.8 + i * 1.0)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.7), Inches(0.85))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_GRAY_BG
        card.line.color.rgb = COLOR_BORDER
        
        tf = card.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{num}   |   {h}  —  {sub}"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY

    # SLIDE 3: Results Table
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Bảng Đối Chiếu Hiệu Năng Thực Nghiệm", "KẾT QUẢ")
    
    rows, cols = 5, 4
    tbl_shape = s3.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.5))
    table = tbl_shape.table
    
    headers = ["Phương pháp / Mô hình", "Độ chính xác (Acc)", "Macro F1-Score", "Đặc điểm nổi bật"]
    table_data = [
        ["Hệ chuyên gia (10 Luật Sản khoa)", "82.25%", "0.7410", "Suy diễn tiến & lùi giải thích được 100% ca bệnh"],
        ["Mạng nơ-ron (MLP EarlyStopping)", "88.51%", "0.8240", "Hội tụ sau 42 epochs, kiểm soát overfitting bằng L2"],
        ["Cây quyết định (Decision Tree)", "91.12%", "0.8412", "Cắt tỉa độ sâu max_depth=5 để trích xuất luật"],
        ["Random Forest (150 cây - TỐT NHẤT)", "95.04%", "0.9015", "Đạt chuẩn triển khai lâm sàng, lưu BestModel.joblib"]
    ]
    
    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    for r_idx, row in enumerate(table_data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 0 else COLOR_GRAY_BG
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_TEXT_DARK
            if c_idx in [1, 2]: p.alignment = PP_ALIGN.CENTER

    prs.save(output_path)
    print(f"[+] Successfully generated Academic Slide Deck: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create standardized academic PowerPoint deck.")
    parser.add_argument("--output", default="Slide_ThuyetTrinh_Chuan.pptx")
    parser.add_argument("--title", default="ĐÁNH GIÁ SỨC KHỎE THAI NHI TỪ BIỂU ĐỒ TIM THAI")
    args = parser.parse_args()
    create_slide_deck(args.output, args.title)
