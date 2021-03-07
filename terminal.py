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


def print_first(sorter, bars, columns):
    upper_left_print = "  Terminal Sorting Visualizer by Diego González Liarte"
    upper_right_print = f"Visualizing {sorter}  "
    upper_print = f"{upper_left_print}{(columns - len(upper_left_print) - len(upper_right_print)) * ' '}{upper_right_print}\n\n"

    clear()
    print(upper_print)
    print(create_bars(bars, columns))


def print_step(step, length):
    sys.stdout.write(f"\u001b[{length}A")  # Moves stdout cursor to beginning of printed bars
    print(step)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
