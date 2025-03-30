import os
import subprocess
import sys

def build_executable():
    """使用 PyInstaller 打包程序"""
    print("🚀 开始打包程序...")
    
    # 安装必要的依赖
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    
    # 使用 PyInstaller 打包
    subprocess.check_call([
        "pyinstaller",
        "--onefile",
        "--name=binary_hex_trainer",
        "--add-data=README.md;.",
        "binary_hex_trainer.py"
    ])
    
    print("✨ 打包完成！")
    print("📦 可执行文件位置：dist/binary_hex_trainer.exe")
    print("\n使用说明：")
    print("1. 直接双击 dist 文件夹中的 binary_hex_trainer.exe")
    print("2. 无需安装 Python 或其他依赖")
    print("3. 可以创建快捷方式到桌面")

if __name__ == "__main__":
    build_executable() 