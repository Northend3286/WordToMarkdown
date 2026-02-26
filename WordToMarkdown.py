import os
import subprocess
import sys

def get_pandoc_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, "pandoc.exe")

def convert_docx(filepath):
    filename, _ = os.path.splitext(filepath)
    output_file = filename + ".md"
    media_dir = filename + "_media"  # 图片输出目录
    os.makedirs(media_dir, exist_ok=True)
    pandoc_path = get_pandoc_path()
    subprocess.run([
        pandoc_path,
        filepath,
        "-o", output_file,
        "--extract-media", media_dir
    ], check=True)

def main():
    print("=== Word 批量转 Markdown 工具 ===\n")

    current_dir = os.getcwd()
    files = os.listdir(current_dir)

    docx_files = [f for f in files if f.lower().endswith(".docx")]

    if not docx_files:
        print("当前文件夹没有找到 .docx 文件")
        input("\n按回车键退出...")
        return

    print(f"找到 {len(docx_files)} 个 Word 文件，开始转换...\n")

    for file in docx_files:
        convert_docx(file)

    print("\n全部转换完成！")
    input("\n按回车键退出...")

if __name__ == "__main__":
    main()