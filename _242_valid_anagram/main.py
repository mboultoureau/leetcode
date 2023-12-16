class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 2
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

        # Solution 1
        # if len(s) != len(t):
        #     return False

        # letters = {}

        # for c in s:
        #     if c in letters:
        #         letters[c] += 1
        #     else:
        #         letters[c] = 1

        # for c in t:
        #     if c not in letters or letters[c] == 0:
        #         return False
        #     else:
        #         letters[c] -= 1

        # return True