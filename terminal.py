import os


def create_bars(bars, columns):
    l = len(bars)
    message = ""
    for i, _ in enumerate(range(l)):
        message += " " * ((columns - l * 2) // 2)
        for bar in bars:
            message += "██" if bar >= l - i else "  "
        message += "\n"
    return message

def print_screen(bars, upper_print, columns):
    clear()
    print(upper_print)
    print(create_bars(bars, columns))

def clear():
    os.system('cls')