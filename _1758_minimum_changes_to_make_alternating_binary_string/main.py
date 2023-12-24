class Solution:
    def minOperations(self, s: str) -> int:
        nb1 = 0
        nb2 = 0

        for i in range(len(s)):
            if (i % 2 == 0 and s[i] != '0') or (i % 2 == 1 and s[i] != '1'):
                nb1 += 1
            elif (i % 2 == 0 and s[i] != '1') or (i % 2 == 1 and s[i] != '0'):
                nb2 += 1

        return min(nb1, nb2)