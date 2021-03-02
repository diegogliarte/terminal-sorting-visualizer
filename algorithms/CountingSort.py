from algorithms.Sort import Sort


def countSort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i - 1]
    print(count)


class CountingSort(Sort):

    def __str__(self):
        return "Counting Sort"

    def sort(self):
        if not self.array: return

        output = [0 for _ in self.array]

        count = []
        for i in range(max(self.array) + 1):
            count.append(self.array.count(i))
            if i != 0: count[i] += count[i - 1]

        for idx, e in enumerate(self.array[:]):
            self.array[count[e] - 1] = e
            self.steps.append(self.array[:])
            count[e] -= 1

arr = [1, 4, 1, 2, 7, 5, 2]
# arr2 = '1412752'
# countSort(arr2)
sorter = CountingSort(arr)
sorter.sort()
print(sorter.array)
