class MedianFinder:

    def __init__(self):
        self.lower = []
        self.higher = []
        

    def addNum(self, num: int) -> None:
        if self.higher and num > self.higher[0]:
            heapq.heappush(self.higher, num)
        else:
            heapq.heappush(self.lower, -1 * num)

        if len(self.higher) > len(self.lower) + 1:
            n = -1 * heapq.heappop(self.higher)
            heapq.heappush(self.lower, n)
        elif len(self.lower) > len(self.higher) + 1:
            n = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.higher, n)
        

    def findMedian(self) -> float:
        if len(self.higher) > len(self.lower):
            return self.higher[0]
        elif len(self.higher) < len(self.lower):
            return -1 * self.lower[0]
        else:
            return (-1 * self.lower[0] + self.higher[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()