import os
import subprocess
import sys
import platform

def build_executable():
    """使用 PyInstaller 打包程序"""
    try:
        print("[BUILD] Starting build process...")
        
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
        
        print("[SUCCESS] Build completed!")
        print("[INFO] Executable location: dist/binary_hex_trainer" + (".exe" if platform.system() == 'Windows' else ""))
        print("\nUsage instructions:")
        if platform.system() == 'Windows':
            print("1. Double click binary_hex_trainer.exe in the dist folder")
            print("2. No Python or dependencies required")
            print("3. You can create a desktop shortcut")
        else:
            print("1. Run in terminal:")
            print("   chmod +x dist/binary_hex_trainer")
            print("   ./dist/binary_hex_trainer")
            print("2. Or create a desktop shortcut")
    except Exception as e:
        print(f"[ERROR] Error during build: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    build_executable() 