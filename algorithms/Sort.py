class Sort():
    def __init__(self, array=None):
        if array == None: array = []
        self.array = array
        self.steps = []

    def __call__(self, array):
        self.array = array
        self.steps = []

    def __str__(self):
        return "Sort"

    def solve(self):
        pass
