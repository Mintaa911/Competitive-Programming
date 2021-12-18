class RecentCounter:
    
    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        idx = len(self.counter)-1
        c = 0
        while idx > -1 and self.counter[idx] >= (t - 3000):
            c += 1
            idx -= 1
        return c