class QuickSort():

    def __init__(self, array):
        self.array = array
        self.steps = []

    def __str__(self):
        return "Quick Sort"

    def sort(self, low=0, high=None):
        high = len(self.array) - 1 if high == None else high
        if (low > high): return
        pi = self._partition(low, high)

        self.sort(low, pi - 1)
        self.sort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[j], self.array[i] = self.array[i], self.array[j]
                self.steps.append(self.array[:])

        self.array[high], self.array[i + 1] = self.array[i + 1], self.array[high]
        self.steps.append(self.array[:])

        return i + 1
