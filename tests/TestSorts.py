import unittest
import random
import time
from algorithms.SelectionSort import SelectionSort
from algorithms.BubbleSort import BubbleSort
from algorithms.InsertionSort import InsertionSort
from algorithms.MergeSort import MergeSort
from algorithms.QuickSort import QuickSort
from algorithms.HeapSort import HeapSort


class TestSorts(unittest.TestCase):
    empty = []
    single = [1]
    pair = [1, 0]
    ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unordered = [1, 4, 7, 5, 2, 8, 9, 3, 6]
    big = list(range(750))
    random.shuffle(big)

    def test_all(self):
        algorithms = [SelectionSort, BubbleSort, InsertionSort, MergeSort, QuickSort, HeapSort]
        for algorithm in algorithms:
            sorter = algorithm()
            tic = time.time()
            self._test_sorts(sorter)
            print(f"{sorter} ran in {time.time() - tic} s")

        self.assertTrue(True)  # So the last print can be printed nicely

    def _test_sorts(self, sorter):
        for k, v in vars(TestSorts).items():
            if not hasattr(v,
                           '__call__') and "_" not in k:  # Be careful with this in case you use underscored variables
                sorter(v[:])
                sorter.sort()
                self.assertEqual(sorted(v), sorter.array, f"{sorter} failed with {k} array!")
