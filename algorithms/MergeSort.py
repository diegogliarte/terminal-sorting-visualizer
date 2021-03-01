from algorithms.Sort import Sort


class MergeSort(Sort):

    def __str__(self):
        return "Merge Sort"

    def sort(self, array=None):
        array = array or self.array
        if len(array) <= 1: return array

        left = self.sort(array[:len(array) // 2])
        right = self.sort(array[len(array) // 2:])
        result = self._merge(left, right)
        return result

    def _merge(self, left, right):
        result = []
        first_idx = self.array.index(left[0])
        while left and right:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        result += left + right
        for idx, e in enumerate(result):
            self.array[first_idx + idx] = e
            self.steps.append(self.array[:])

        return result
