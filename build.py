import os
import subprocess
import sys
import platform

# 设置控制台编码为 UTF-8
if platform.system() == 'Windows':
    os.system('chcp 65001')  # 设置 Windows 控制台为 UTF-8 编码
else:
    os.environ['PYTHONIOENCODING'] = 'utf-8'  # 设置 Python IO 编码为 UTF-8
    sys.stdout.reconfigure(encoding='utf-8')  # 设置标准输出编码为 UTF-8

def build_executable():
    """使用 PyInstaller 打包程序"""
    print("🚀 开始打包程序...")
    
    # 安装必要的依赖
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    
    # 根据操作系统选择路径分隔符
    separator = ';' if platform.system() == 'Windows' else ':'
    
    # 使用 PyInstaller 打包
    subprocess.check_call([
        "pyinstaller",
        "--onefile",
        "--name=binary_hex_trainer",
        f"--add-data=README.md{separator}.",
        "binary_hex_trainer.py"
    ])
    
    print("✨ 打包完成！")
    print("📦 可执行文件位置：dist/binary_hex_trainer" + (".exe" if platform.system() == 'Windows' else ""))
    print("\n使用说明：")
    if platform.system() == 'Windows':
        print("1. 直接双击 dist 文件夹中的 binary_hex_trainer.exe")
        print("2. 无需安装 Python 或其他依赖")
        print("3. 可以创建快捷方式到桌面")
    else:
        print("1. 在终端中运行：")
        print("   chmod +x dist/binary_hex_trainer")
        print("   ./dist/binary_hex_trainer")
        print("2. 或者创建桌面快捷方式")

if __name__ == "__main__":
    build_executable() 