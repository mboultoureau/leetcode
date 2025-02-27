class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0
        nums = set(arr)

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev = arr[i]
                curr = arr[j]
                nxt = prev + curr
                length = 2

                while nxt in nums:
                    prev = curr
                    curr = nxt
                    nxt = prev + curr
                    length += 1
                    result = max(result, length)

        return result
