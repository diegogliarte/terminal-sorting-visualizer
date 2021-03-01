from algorithms.Sort import Sort


class BubbleSort(Sort):

    def __str__(self):
        return "Bubble Sort"

    def sort(self):
        sorted_ = False
        while not sorted_:
            sorted_ = True
            for idx, e in enumerate(self.array[1:]):
                if e < self.array[idx]:
                    sorted_ = False
                    self.array[idx], self.array[idx + 1] = self.array[idx + 1], self.array[idx]
                    self.steps.append(self.array[:])
