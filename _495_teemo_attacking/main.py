class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        
        result = 0

        for i in range(len(timeSeries) - 1):
            result += min(timeSeries[i + 1] - timeSeries[i], duration)

        return result + duration