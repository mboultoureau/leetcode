class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_pile = max(candies)
        left = 0
        right = max_pile

        while left < right:
            middle = (left + right + 1) // 2
            
            # Check if possible
            children = 0
            for pile in candies:
                children += pile // middle

            if children >= k:
                left = middle
            else:
                right = middle - 1

        return left