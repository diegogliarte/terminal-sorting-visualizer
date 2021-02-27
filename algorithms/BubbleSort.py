class BubbleSort():

    def __init__(self, array):
        self.array = array
        self.steps = []

    def sort(self):
        sorted_ = False
        while not sorted_:
            sorted_ = True
            for idx, e in enumerate(self.array[1:]):
                if e < self.array[idx]:
                    sorted_ = False
                    self.array[idx], self.array[idx + 1] = self.array[idx + 1], self.array[idx]
                    self.steps.append(self.array[:])

