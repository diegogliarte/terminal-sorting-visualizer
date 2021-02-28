class SelectionSort():

    def __init__(self, array):
        self.array = array
        self.steps = []

    def __str__(self):
        return "Selection Sort"

    def sort(self):
        for i in range(len(self.array)):
            min_ = min((val, idx + i) for idx, val in enumerate(self.array[i:]))[
                1]  # Iterates from position i to len. Val is used for the min, we get the idx.
            self.array[min_], self.array[i] = self.array[i], self.array[min_]
            self.steps.append(self.array[:])
