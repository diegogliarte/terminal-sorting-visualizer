import unittest
import random
import time
from algorithms.Algorithms import Algorithms



class TestSorts(unittest.TestCase):
    empty = []
    single = [1]
    pair = [1, 0]
    ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unordered = [1, 4, 7, 5, 2, 8, 9, 3, 6]
    big = list(range(750))
    r = [5, 3, 8, 9, 1, 4, 7, 2, 6]
    random.shuffle(big)

    def test_all(self):
        for algorithm in Algorithms.get_algorithms().values():
            sorter = algorithm()
            tic = time.time()
            self._test_sorts(sorter)
            print(f"{sorter} succeeded in {time.time() - tic} s")

        # So the last print can be printed nicely
        time.sleep(1 * 10 ** -10)
        self.assertTrue(True)

    def _test_sorts(self, sorter):
        for k, v in vars(TestSorts).items():
            if not hasattr(v,
                           '__call__') and "_" not in k:  # Be careful with this in case you use underscored variables
                sorter(v[:])
                sorter.sort()
                self.assertEqual(sorted(v), sorter.array, f"{sorter} failed with {k} array!")
