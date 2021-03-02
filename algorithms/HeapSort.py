from algorithms.Sort import Sort


class HeapSort(Sort):

    def __str__(self):
        return "Heap Sort"

    def sort(self):
        n = len(self.array)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.steps.append(self.array[:])
            self._heapify(i, 0)

    def _heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.array[largest] < self.array[l]:
            largest = l

        if r < n and self.array[largest] < self.array[r]:
            largest = r

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.steps.append(self.array[:])
            self._heapify(n, largest)

