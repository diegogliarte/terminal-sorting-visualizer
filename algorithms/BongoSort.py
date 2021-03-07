from algorithms.Sort import Sort
import random


class BongoSort(Sort):

    def __str__(self):
        return "Bongo Sort"

    def sort(self):
        l = len(self.array)
        while self.array != sorted(self.array):
            idx1 = random.randrange(l)
            idx2 = random.randrange(l)
            self.array[idx1], self.array[idx2] = self.array[idx2], self.array[idx1]
            yield self.array
