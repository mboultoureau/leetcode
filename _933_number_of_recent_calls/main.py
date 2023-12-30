class RecentCounter:
    # Solution 2
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        count = 0
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)

    # Solution 1
    # def __init__(self):
    #     self.requests = []

    # def ping(self, t: int) -> int:
    #     self.requests.append(t)
    #     count = 0
    #     for i in range(len(self.requests) - 1, -1, -1):
    #         if t - self.requests[i] <= 3000:
    #             count += 1
    #         else:
    #             return count

    #     return count      


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)