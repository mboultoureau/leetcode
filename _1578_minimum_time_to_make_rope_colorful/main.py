class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        
        while left < len(colors):
            total = 0
            maximum = 0
            while right < len(colors) and colors[left] == colors[right]:
                total += neededTime[right]
                maximum = max(neededTime[right], maximum)
                right += 1

            if right - left > 1:
                result += total - maximum

            left = right

        return result