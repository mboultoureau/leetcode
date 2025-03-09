class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        groups = 0
        left = 0
        right = 0

        while left < len(colors):
            right += 1
            if colors[(right - 1) % len(colors)] == colors[right % len(colors)]:
                left = right
                continue

            if right - left == k - 1:
                groups += 1
                left += 1

        return groups