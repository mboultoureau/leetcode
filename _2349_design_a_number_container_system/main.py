class NumberContainers:

    def __init__(self):
        self.nums_to_idx = defaultdict(list)
        self.idx_to_nums = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        heapq.heappush(self.nums_to_idx[number], index)
        self.idx_to_nums[index] = number

    def find(self, number: int) -> int:
        length = len(self.nums_to_idx[number])
        for _ in range(length):
            index = self.nums_to_idx[number][0]
            if self.idx_to_nums[index] == number:
                return index

            heapq.heappop(self.nums_to_idx[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)