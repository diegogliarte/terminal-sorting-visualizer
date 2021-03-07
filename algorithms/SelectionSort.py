from algorithms.Sort import Sort


class SelectionSort(Sort):

    def __str__(self):
        return "Selection Sort"

    def sort(self):
        for i in range(len(self.array)):
            min_ = min((val, idx + i) for idx, val in enumerate(self.array[i:]))[
                1]
            self.array[min_], self.array[i] = self.array[i], self.array[min_]
            self.steps.append(self.array[:])
