class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        currentSum = 0
        count = 0

        for i in range(1, n + 1):
            if i in banned:
                continue

            if i + currentSum > maxSum:
                break

            currentSum += i
            count += 1

        return count