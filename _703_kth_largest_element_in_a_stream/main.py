class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.maxs = [float("-inf") for _ in range(k)]

        nums.sort(reverse=True)
        for i in range(min(k, len(nums))):
            self.maxs[i] = nums[i]

        print(self.maxs)

    def add(self, val: int) -> int:
        self.nums.append(val)
        if val > self.maxs[-1]:
            self.maxs.pop()

            index = 0
            while index < len(self.maxs) and self.maxs[index] > val:
                index += 1

            self.maxs.insert(index, val)

        return self.maxs[self.k - 1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)