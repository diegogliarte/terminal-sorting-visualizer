class InsertionSort():

    def __init__(self, array):
        self.array = array
        self.steps = []

    def __str__(self):
        return "Insertion Sort"

    def sort(self):
        for i in range(1, len(self.array)):
            for j, e in enumerate(reversed(self.array[:i])):
                if not e > self.array[i - j]:
                    break

                self.array[i - j], self.array[i - j - 1] = self.array[i - j - 1], self.array[i - j]
                self.steps.append(self.array[:])
