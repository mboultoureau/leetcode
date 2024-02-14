class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        for num in nums:
            if num >= 0:
                positives.append(num)
            else:
                negatives.append(num)

        nums = []
        for i in range(len(positives)):
            nums.append(positives[i])
            nums.append(negatives[i])

        return nums