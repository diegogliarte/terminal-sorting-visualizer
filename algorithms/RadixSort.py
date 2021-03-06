from algorithms.Sort import Sort


class RadixSort(Sort):

    def __str__(self):
        return "Radix Sort"

    def countingSort(self, exp1):
        n = len(self.array)

        output = self.array[:]

        count = []
        digits = [int((e / exp1) % 10) for e in self.array]
        for i in range(10):
            count.append(digits.count(i))
            if i != 0: count[i] += count[i - 1]

        for idx, e in enumerate(reversed(self.array[:])):
            index = (e / exp1)
            output[count[int(index % 10)] - 1] = self.array[n - idx - 1]
            self.steps.append(output[:])
            count[int(index % 10)] -= 1

        self.array = output

    def sort(self):
        if not self.array: return
        max_digits = len(str(max(self.array)))

        exp = 1
        for i in range(max_digits):
            self.countingSort(exp)
            exp *= 10