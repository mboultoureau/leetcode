class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # SOLUTION 2
        vowels = [-1, -1, -1]
        substrings = 0

        for i in range(len(s)):
            vowels[ord(s[i]) - ord('a')] = i
            substrings += 1 + min(vowels)

        return substrings


        ## SOLUTION 1
        # left = 0
        # right = 0
        # substrings = 0
        # vowels = defaultdict(int)

        # while right < len(s):
        #     vowels[s[right]] += 1

        #     while vowels['a'] > 0 and vowels['b'] > 0 and vowels['c'] > 0:
        #         substrings += len(s) - right
        #         vowels[s[left]] -= 1
        #         left += 1

        #     right += 1

        # return substrings