class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Solution 2
        letters = Counter(s)

        result = 0
        for _, v in letters.items():
            result += v // 2

        result *= 2

        if result == len(s):
            return result
        else:
            return result + 1


        # Solution 1
        # letters = {}

        # for c in s:
        #     if c in letters:
        #         letters[c] += 1
        #     else:
        #         letters[c] = 1

        # result = 0
        # for _, v in letters.items():
        #     result += v // 2

        # result *= 2

        # if result == len(s):
        #     return result
        # else:
        #     return result + 1
