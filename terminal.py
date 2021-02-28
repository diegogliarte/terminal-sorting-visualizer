import os
import sys

def create_bars(bars, columns):
    l = len(bars)
    message = ""
    for i, _ in enumerate(range(l)):
        message += " " * ((columns - l * 2) // 2)
        for bar in bars:
            message += "██" if bar >= l - i else "  "
        message += "\n"
    return message

def print_first(upper_print, bars, columns):
    clear()
    print(upper_print)
    print(create_bars(bars, columns))

def print_step(initial_bar, step):
    sys.stdout.write(f"\u001b[{len(initial_bar) + 1}A")  # Moves stdout cursor to beginning of printed bars
    print(step)


def clear():
    os.system('cls')