import os
import sys
from pathlib import Path

try:
    import pypandoc
except ImportError:
    print("未安装 pypandoc，请先安装 Pandoc 和 pypandoc")
    sys.exit(1)

# 获取 exe 或脚本所在目录
if getattr(sys, 'frozen', False):
    # PyInstaller 打包后
    base_dir = Path(sys.executable).parent
else:
    # 普通 Python
    base_dir = Path(__file__).parent

# 输出目录
output_dir = base_dir / "Markdown_output"
output_dir.mkdir(exist_ok=True)

# 支持的文件类型
extensions = [".docx", ".pdf"]

# 遍历目录中的文件
for file in base_dir.iterdir():
    if file.suffix.lower() in extensions:
        md_name = output_dir / (file.stem + ".md")
        try:
            # 使用 pypandoc 转换
            output = pypandoc.convert_file(str(file), 'md', format='docx' if file.suffix.lower() == '.docx' else 'pdf')
            with md_name.open("w", encoding="utf-8") as f:
                f.write(output)
            print(f"生成: {md_name.name}")
        except Exception as e:
            print(f"转换失败: {file.name}, 错误: {e}")

print(f"\n所有文件已处理完成，输出目录: {output_dir}")
input("按 Enter 键退出...")
