#!/usr/bin/env python3
"""
Mermaid Diagram Compiler CLI Helper.
Renders Mermaid diagram strings or .mmd files to crisp PNG / SVG / PDF using @mermaid-js/mermaid-cli.
"""

import sys
import os
import subprocess
import argparse
import tempfile
import shutil

DEFAULT_MERMAID = """flowchart TD
    A["Raw CTG Data"] --> B["Preprocessing & Scaling"]
    B --> C["Feature Selection"]
    C --> D["Random Forest Classifier"]
    D --> E["Clinical Diagnosis (3 Classes)"]
"""

def render_mermaid(mmd_content: str, output_path: str = "diagram.png", scale: int = 3):
    # Write content to temporary .mmd file
    with tempfile.NamedTemporaryFile("w", suffix=".mmd", delete=False, encoding="utf-8") as f:
        f.write(mmd_content)
        temp_input = f.name

    try:
        # Detect npx executable name on Windows
        npx_cmd = shutil.which("npx") or "npx"
        cmd = [
            npx_cmd, "--yes", "-p", "@mermaid-js/mermaid-cli", "mmdc",
            "-i", temp_input,
            "-o", output_path,
            "-b", "white",
            "-s", str(scale)
        ]
        print(f"[*] Compiling Mermaid diagram to {output_path} (Scale {scale}x)...")
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=(os.name == 'nt'))
        print(f"[+] Successfully rendered diagram: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Compilation error from mmdc: {e.stderr or e.stdout}")
        return False
    except Exception as e:
        print(f"[-] Execution failed: {e}")
        return False
    finally:
        if os.path.exists(temp_input):
            os.remove(temp_input)

def main():
    parser = argparse.ArgumentParser(description="Render Mermaid diagrams to PNG/SVG.")
    parser.add_argument("input", nargs="?", help="Input .mmd file or raw Mermaid text")
    parser.add_argument("--output", "-o", default="diagram.png", help="Output image path (.png, .svg, .pdf)")
    parser.add_argument("--scale", "-s", type=int, default=3, help="Resolution scale factor (default: 3)")
    args = parser.parse_args()

    if args.input and os.path.isfile(args.input):
        with open(args.input, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.input:
        content = args.input
    elif not sys.stdin.isatty():
        content = sys.stdin.read().strip()
    else:
        content = DEFAULT_MERMAID

    render_mermaid(content, args.output, args.scale)

if __name__ == "__main__":
    main()
