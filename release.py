import os
import shutil
import platform
import subprocess
from datetime import datetime

def create_release():
    """创建发布包"""
    print("🚀 开始创建发布包...")
    
    # 创建发布目录
    release_dir = "release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # 复制可执行文件
    exe_name = "进制转换练习.exe" if platform.system() == 'Windows' else "进制转换练习"
    shutil.copy(f"dist/{exe_name}", release_dir)
    
    # 复制 README
    shutil.copy("README.md", release_dir)
    
    # 创建压缩包
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"进制转换练习_{platform.system()}_{timestamp}"
    
    if platform.system() == 'Windows':
        shutil.make_archive(zip_name, 'zip', release_dir)
    else:
        subprocess.check_call(["zip", "-r", f"{zip_name}.zip", release_dir])
    
    print(f"✨ 发布包创建完成！")
    print(f"📦 发布包位置：{zip_name}.zip")
    print("\n发布包包含：")
    print(f"1. {exe_name}")
    print("2. README.md")
    
    # 清理临时文件
    shutil.rmtree(release_dir)

if __name__ == "__main__":
    create_release() 