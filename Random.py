import random


class Random:
    def __init__(self):
        self.randomEngine = random.Random()

    def rand_uint(self, low=None, high=None):
        if high is None:
            high = low
            low = 0
        return self.randomEngine.randint(low, high)

    def rand_float(self, low=None, high=None):
        if high is None:
            high = low
            low = 0.0
        return self.randomEngine.uniform(low, high)
