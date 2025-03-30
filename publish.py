import os
import shutil
import platform
import subprocess
from datetime import datetime

def build_for_platform():
    """为当前平台构建可执行文件"""
    print(f"🚀 开始为 {platform.system()} 构建...")
    subprocess.check_call([sys.executable, "build.py"])
    print(f"✨ {platform.system()} 构建完成！")

def create_release():
    """创建发布包"""
    print("📦 开始创建发布包...")
    
    # 创建发布目录
    release_dir = "release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # 创建平台特定目录
    platform_dir = os.path.join(release_dir, platform.system().lower())
    os.makedirs(platform_dir)
    
    # 复制可执行文件
    exe_name = "binary_hex_trainer.exe" if platform.system() == 'Windows' else "binary_hex_trainer"
    shutil.copy(f"dist/{exe_name}", platform_dir)
    
    # 复制 README
    shutil.copy("README.md", release_dir)
    
    # 创建压缩包
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"binary_hex_trainer_{platform.system().lower()}_{timestamp}"
    
    if platform.system() == 'Windows':
        shutil.make_archive(zip_name, 'zip', release_dir)
    else:
        subprocess.check_call(["zip", "-r", f"{zip_name}.zip", release_dir])
    
    print(f"✨ 发布包创建完成！")
    print(f"📦 发布包位置：{zip_name}.zip")
    print("\n发布包包含：")
    print(f"1. {platform.system()} 版本可执行文件")
    print("2. README.md")
    
    # 清理临时文件
    shutil.rmtree(release_dir)

def main():
    """主函数"""
    print("🌟 进制转换练习程序发布工具")
    print("=" * 50)
    
    # 构建当前平台版本
    build_for_platform()
    
    # 创建发布包
    create_release()
    
    print("\n🎉 发布完成！")
    print("\n下一步：")
    print("1. 将发布包上传到 GitHub Releases")
    print("2. 更新 README.md 中的下载链接")
    print("3. 分享给其他同学！")

if __name__ == "__main__":
    main() 