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
                  "heap": ("Heap Sort", ),
                  "counting": ("Counting Sort", ),
                  "radix": ("Radix Sort", ),
                  "bucket": ("Bucket Sort", ),
                  }

    algorithm = sys.argv[1].replace("sort", "")

    if algorithm not in algorithms.keys():
        raise SyntaxError("Invalid sorting algorithm.")

    # Initialize parameters
    columns, lines = os.get_terminal_size() # Won't work with an IDE, needs to be run in Console
    colorama.init()

    algorithm, sorter = algorithms[algorithm]

    upper_left_print = "  Terminal Sorting Visualizer by Diego González Liarte"
    upper_right_print = f"Visualizing {algorithm}  "
    upper_print = f"{upper_left_print}{(columns - len(upper_left_print) - len(upper_right_print)) * ' '}{upper_right_print}\n\n"

    # Creates initial randomized array
    initial_bar = list(range(1, int(min(lines * 0.8, (columns * 0.8) / 2))))
    random.shuffle(initial_bar)


    terminal.print_first(upper_print, initial_bar, columns)

    sorter = sorter(initial_bar)
    sorter.sort()

    # Removes duplicates and begins creating the bars
    steps = []
    bars = []
    for step in sorter.steps:
        if step not in steps:
            steps.append(step)
            bars.append(terminal.create_bars(step, columns))

    # Begins to print the sorting steps
    time.sleep(1.5)

    for step in bars:
        terminal.print_step(initial_bar, step)
        time.sleep(0.001)

if __name__ == '__main__':
    main()

