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
    initial_bar = list(range(1, int(min(lines * 0.8, (columns * 0.8) / 2))))
    random.shuffle(initial_bar)

    sorter = algorithm(initial_bar)
    terminal.print_first(sorter, initial_bar, columns)
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
    parser = argparse.ArgumentParser()
    algorithms = [algorithm.lower() for algorithm in vars(Algorithms) if algorithm.isupper()]

    parser.add_argument("algorithm", help="Visualizes said algorithm", choices=algorithms)
    args = parser.parse_args()
    algorithm = vars(args)["algorithm"].upper()  # TODO accept "quick" and "quicksort"
    if algorithm not in vars(Algorithms):
        exit(1)

    exit(main(getattr(Algorithms, algorithm)))
