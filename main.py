#!/usr/bin/env python3
import os
import sys
import colorama
import random
import time
from algorithms.SelectionSort import SelectionSort
from algorithms.BubbleSort import BubbleSort
from algorithms.InsertionSort import InsertionSort
from algorithms.MergeSort import MergeSort
from algorithms.QuickSort import QuickSort
import terminal

def main():
    if len(sys.argv) != 2:
        raise IndexError("Invalid arguments. Make sure it's one of these: selection, bubble, insertion, merge, quick, heap, counting, radix or bucket")

    algorithms = { "selection" : ("Selection Sort", SelectionSort),
                  "bubble": ("Bubble Sort", BubbleSort),
                  "insertion": ("Insertion Sort", InsertionSort),
                  "merge" : ("Merge Sort", MergeSort),
                  "quick": ("Quick Sort", QuickSort),
                  "heap": "Heap Sort",
                  "counting": "Counting Sort",
                  "radix": "Radix Sort",
                  "bucket": "Bucket Sort",
                  }

    if sys.argv[1] not in algorithms.keys():
        raise SyntaxError("Invalid sorting algorithm.")

    terminal.clear()
    columns, lines = os.get_terminal_size()
    colorama.init()

    algorithm, sorter = algorithms[sys.argv[1]]

    upper_left_print = "  Terminal Sorting Visualizer by Diego González Liarte"
    upper_right_print = f"Visualizing {algorithm}  "
    upper_print = f"{upper_left_print}{(columns - len(upper_left_print) - len(upper_right_print)) * ' '}{upper_right_print}\n\n"

    bars = list(range(1, int(min(lines * 0.8, (columns * 0.8) / 2))))
    random.shuffle(bars)

    terminal.print_screen(bars, upper_print, columns)
    sorter = sorter(bars)
    sorter.sort()


    steps = []
    for step in sorter.steps:
        if step not in steps:
            steps.append(step)

    time.sleep(1.5)
    for step in steps:
        sys.stdout.write(f"\u001b[{len(bars) + 1}A") # Moves stdout cursor to beginning of printed bars
        print(terminal.create_bars(step, columns))
        time.sleep(1/1000)

main()


