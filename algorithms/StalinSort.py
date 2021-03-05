from algorithms.Sort import Sort


class StalinSort(Sort):

    def __str__(self):
        return "Stalin Sort"

    def sort(self):
        if not self.array: return
        previous = self.array[0]
        killed = 0
        for i in range(len(self.array)):
            idx = i - killed
            if self.array[idx] < previous:
                self.array[idx] = 0
                self.steps.append(self.array[:])
            else:
                previous = self.array[idx]


