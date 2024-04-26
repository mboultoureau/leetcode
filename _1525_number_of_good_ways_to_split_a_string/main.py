class Solution:
    def numSplits(self, s: str) -> int:
        leftMap = defaultdict(int)
        rightMap = defaultdict(int)

        for c in s:
            rightMap[c] += 1

        result = 0
        for c in s:
            rightMap[c] -= 1
            if rightMap[c] == 0:
                del rightMap[c]

            leftMap[c] += 1

            if len(leftMap) == len(rightMap):
                result += 1

        return result