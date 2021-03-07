#!/usr/bin/env python3
import os
import random
import time
from algorithms.Algorithms import Algorithms
import terminal
import argparse


def main(algorithm):
    # Initialize parameters
    columns, lines = os.get_terminal_size()  # Won't work with an IDE, needs to be run in Console
    n = int(min(lines * 0.85, (columns * 0.85) / 2))
    initial_bar = list(range(1, n))
    random.shuffle(initial_bar)

    sorter = algorithm(initial_bar)
    terminal.print_first(sorter, initial_bar, columns)
    if algorithm == Algorithms.BONGO:
        time.sleep(1.5)
        bongo(sorter, columns, n)
    sorter.sort()

    # Removes duplicates and begins creating the bars
    steps = []
    bars = []
    for step in sorter.steps:
        if step not in steps:
            steps.append(step)
            bars.append(terminal.create_bars(step, columns))
            if step == sorter.array:  # Used in cases such as HeapSort, where the algorithm continues even when the array is already sorted
                break
    # Begins to print the sorting steps

    time.sleep(1.5)
    for bar in bars:
        terminal.print_step(bar, n)
        time.sleep(0.001)


def bongo(sorter, columns, n):
    for step in sorter.sort():
        bar = terminal.create_bars(step, columns)
        terminal.print_step(bar, n)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    algorithms = Algorithms.get_algorithms()
    parser.add_argument("algorithm", help="Visualizes said algorithm", choices=algorithms)
    args = parser.parse_args()
    algorithm = vars(args)["algorithm"].upper()  # TODO accept "quick" and "quicksort"
    if algorithm not in vars(Algorithms):
        exit(1)

    exit(main(getattr(Algorithms, algorithm)))
