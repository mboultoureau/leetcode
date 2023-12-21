class Solution:
    def partitionString(self, s: str) -> int:
        count = {}

        partition = 1
        for c in s:
            if c in count:
                partition += 1
                count = {}
                count[c] = 1
            else:
                count[c] = 1

        return partition