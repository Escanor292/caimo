#!/usr/bin/env python3
"""
Interactive Testing & Demo Launcher for Skills Toolkit.
Allows the user to easily test and explore all humanizer and publishing capabilities in 1 click.
"""

import sys
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def print_banner():
    print("=" * 68)
    print("      SKILLS TOOLKIT - DEMO & TRẢI NGHIỆM CÔNG CỤ TỰ ĐỘNG HÓA")
    print("=" * 68)
    print("1. [Soi lỗi AI] Kiểm tra một đoạn văn tiếng Việt có mùi AI")
    print("2. [Soi lỗi AI] Kiểm tra một đoạn văn tiếng Anh học thuật")
    print("3. [Humanize] Tự động làm sạch & khử danh từ hóa (De-AI)")
    print("4. [SciencePlots] Xuất biểu đồ chuẩn bài báo quốc tế IEEE (300 DPI)")
    print("5. [python-docx] Tạo nhanh file Word báo cáo đồ án mẫu (.docx)")
    print("6. [python-pptx] Tạo nhanh bộ Slide thuyết trình 16:9 mẫu (.pptx)")
    print("7. [Tùy chỉnh] Nhập đoạn văn của riêng bạn để kiểm tra")
    print("0. Thoát")
    print("=" * 68)

def run_option(choice):
    py = sys.executable

    if choice == "1":
        sample = "Trong bối cảnh hiện nay, trí tuệ nhân tạo đóng vai trò vô cùng quan trọng. Không thể phủ nhận rằng công nghệ này phát triển nhanh chóng. Tóm lại, việc ứng dụng AI là một bước tiến mang tính đột phá."
        script = os.path.join(BASE_DIR, "01_AI_Text_Humanizer", "scripts", "text_stats.py")
        subprocess.run([py, script, sample])

    elif choice == "2":
        sample = "It is important to remember that we conducted an investigation into the algorithm. It is clearly evident that AI plays a crucial role. Furthermore, the model makes an assumption that data is normal."
        script = os.path.join(BASE_DIR, "01_AI_Text_Humanizer", "scripts", "text_stats.py")
        subprocess.run([py, script, sample])

    elif choice == "3":
        sample = "Trong bối cảnh hiện nay, chúng tôi tiến hành thực hiện việc phân tích dữ liệu rất cẩn thận. Không thể phủ nhận rằng công nghệ này vô cùng phức tạp."
        script = os.path.join(BASE_DIR, "01_AI_Text_Humanizer", "scripts", "humanize_text.py")
        subprocess.run([py, script, sample])

    elif choice == "4":
        out_path = os.path.join(BASE_DIR, "demo_ieee_plot.png")
        script = os.path.join(BASE_DIR, "02_Academic_Report_and_Slides", "scripts", "make_ieee_plot.py")
        subprocess.run([py, script, "--output", out_path])
        print(f"\n[+] Đã xuất file ảnh IEEE tại: {out_path}")

    elif choice == "5":
        out_path = os.path.join(BASE_DIR, "demo_baocao.docx")
        script = os.path.join(BASE_DIR, "02_Academic_Report_and_Slides", "scripts", "build_academic_doc.py")
        subprocess.run([py, script, "--output", out_path])
        print(f"\n[+] Đã tạo file Word báo cáo tại: {out_path}")

    elif choice == "6":
        out_path = os.path.join(BASE_DIR, "demo_slide.pptx")
        script = os.path.join(BASE_DIR, "02_Academic_Report_and_Slides", "scripts", "build_deck_pptx.py")
        subprocess.run([py, script, "--output", out_path])
        print(f"\n[+] Đã tạo file Slide PowerPoint tại: {out_path}")

    elif choice == "7":
        user_text = input("\nNhập đoạn văn của bạn (nhấn Enter để phân tích): ").strip()
        if user_text:
            script = os.path.join(BASE_DIR, "01_AI_Text_Humanizer", "scripts", "text_stats.py")
            subprocess.run([py, script, user_text])
        else:
            print("[-] Bạn chưa nhập đoạn văn nào.")

def main():
    if len(sys.argv) > 1:
        run_option(sys.argv[1])
        return

    while True:
        print_banner()
        c = input("Chọn chức năng (0-7): ").strip()
        if c == "0":
            print("Tạm biệt!")
            break
        elif c in [str(i) for i in range(1, 8)]:
            print("\n" + "-" * 68)
            run_option(c)
            print("-" * 68 + "\n")
            input("Nhấn Enter để tiếp tục...")
        else:
            print("[-] Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
