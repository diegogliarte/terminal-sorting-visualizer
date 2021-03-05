from algorithms.Sort import Sort


class CountingSort(Sort):

    def __str__(self):
        return "Counting Sort"

    def sort(self):
        if not self.array: return
        count = []
        for i in range(max(self.array) + 1):
            count.append(self.array.count(i))
            if i != 0: count[i] += count[i - 1]

        for idx, e in enumerate(self.array[:]):
            self.array[count[e] - 1] = e
            self.steps.append(self.array[:])
            count[e] -= 1
