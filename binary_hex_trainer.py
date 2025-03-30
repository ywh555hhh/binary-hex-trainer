#!/usr/bin/env python3
import random
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint

console = Console()

# 一些俏皮话
FUNNY_MESSAGES = {
    'correct': [
        "🎉 太棒了！408考试又多了一分！",
        "🌟 完美！你的进制转换速度比CPU还快！",
        "💫 哇！你让计算机组成原理变得如此简单！",
        "🎯 一击即中！你的思维比冯诺依曼还清晰！",
        "🌈 太厉害了！你让数字在内存中跳舞！",
        "🚀 你的进制转换速度比DMA还快！",
        "💡 你的大脑比ALU还强大！",
        "🎓 这就是408考生的实力！"
    ],
    'wrong': [
        "🤔 别灰心！王道的同学也曾经算错过！",
        "💪 差一点点！记住：408考试就是细节的较量！",
        "🎭 没关系！让我们继续练习！",
        "🌱 每个错误都是通向408高分的阶梯！",
        "🎨 计算机组成原理就像艺术，需要不断练习！",
        "📚 复习王道教材，再来一次！",
        "🎯 408考试就是细节的积累！",
        "💫 错误是通向成功的必经之路！"
    ]
}

def generate_random_binary():
    """生成一个8位随机二进制数"""
    return ''.join(random.choice(['0', '1']) for _ in range(8))

def generate_random_hex():
    """生成一个2位随机十六进制数"""
    return hex(random.randint(0, 255))[2:].upper().zfill(2)

def binary_to_hex(binary):
    """将二进制数转换为十六进制"""
    return hex(int(binary, 2))[2:].upper().zfill(2)

def hex_to_binary(hex_num):
    """将十六进制数转换为二进制"""
    return bin(int(hex_num, 16))[2:].zfill(8)

def get_random_message(category):
    """获取随机俏皮话"""
    return random.choice(FUNNY_MESSAGES[category])

def practice_binary_to_hex():
    """练习二进制转十六进制"""
    while True:
        binary = generate_random_binary()
        console.print(Panel(
            f"[bold]请将以下二进制数转换为十六进制：[/bold]\n"
            f"[cyan]{binary}[/cyan]\n"
            f"[yellow]输入 'r' 返回主菜单，输入 'q' 退出程序[/yellow]",
            title="[bold yellow]二进制转十六进制练习[/bold yellow]",
            border_style="green"
        ))

        answer = Prompt.ask("[bold]请输入你的答案[/bold]")
        
        if answer.lower() == 'q':
            return 'quit'
        elif answer.lower() == 'r':
            return 'return'
        
        correct_hex = binary_to_hex(binary)
        
        if answer.upper() == correct_hex:
            console.print(Panel(
                f"[bold green]{get_random_message('correct')}[/bold green]",
                border_style="green"
            ))
        else:
            console.print(Panel(
                f"[bold red]{get_random_message('wrong')}[/bold red]\n"
                f"[yellow]正确答案是：[/yellow] [cyan]{correct_hex}[/cyan]",
                border_style="red"
            ))

def practice_hex_to_binary():
    """练习十六进制转二进制"""
    while True:
        hex_num = generate_random_hex()
        console.print(Panel(
            f"[bold]请将以下十六进制数转换为二进制：[/bold]\n"
            f"[cyan]{hex_num}[/cyan]\n"
            f"[yellow]输入 'r' 返回主菜单，输入 'q' 退出程序[/yellow]",
            title="[bold yellow]十六进制转二进制练习[/bold yellow]",
            border_style="green"
        ))

        answer = Prompt.ask("[bold]请输入你的答案[/bold]")
        
        if answer.lower() == 'q':
            return 'quit'
        elif answer.lower() == 'r':
            return 'return'
        
        correct_binary = hex_to_binary(hex_num)
        
        if answer == correct_binary:
            console.print(Panel(
                f"[bold green]{get_random_message('correct')}[/bold green]",
                border_style="green"
            ))
        else:
            console.print(Panel(
                f"[bold red]{get_random_message('wrong')}[/bold red]\n"
                f"[yellow]正确答案是：[/yellow] [cyan]{correct_binary}[/cyan]",
                border_style="red"
            ))

def main():
    while True:
        console.print(Panel.fit(
            "[bold cyan]🌟 欢迎使用408进制转换练习程序！🌟[/bold cyan]\n"
            "[yellow]让我们开始有趣的数字转换之旅吧！[/yellow]\n"
            "[italic]作者：teapot1de[/italic]",
            title="[bold green]408进制转换训练器[/bold green]",
            border_style="blue"
        ))

        console.print("\n[bold]请选择练习模式：[/bold]")
        console.print("1. [cyan]二进制转十六进制[/cyan]")
        console.print("2. [cyan]十六进制转二进制[/cyan]")
        console.print("3. [red]退出程序[/red]")
        
        choice = Prompt.ask("[bold]请输入你的选择 (1-3)[/bold]")
        
        if choice == '1':
            result = practice_binary_to_hex()
            if result == 'quit':
                break
        elif choice == '2':
            result = practice_hex_to_binary()
            if result == 'quit':
                break
        elif choice == '3':
            console.print(Panel(
                "[bold yellow]👋 感谢使用！下次再见！[/bold yellow]\n"
                "[italic]记住：408考试就是细节的积累！[/italic]\n"
                "[italic]作者：teapot1de[/italic]",
                border_style="blue"
            ))
            break
        else:
            console.print("[bold red]❌ 无效的选择，请重试！[/bold red]")

if __name__ == "__main__":
    main() 