class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Solution 2
        frequency = defaultdict(int)
        max_frequency = 0
        result = 0

        for n in nums:
            frequency[n] += 1
            max_frequency = max(max_frequency, frequency[n])

        for v in frequency.values():
            if v == max_frequency:
                result += v

        return result

        # Solution 1
        # count = Counter(nums)
        # max_frequency = max(count.values())
        # result = 0

        # for v in count.values():
        #     if v == max_frequency:
        #         result += v

        # return result