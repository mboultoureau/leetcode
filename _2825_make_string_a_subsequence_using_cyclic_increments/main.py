class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            letter1 = (ord(str1[i]) - ord('a') + 1) % 26
            letter2 = ord(str2[j]) - ord('a')

            if str1[i] == str2[j] or letter1 == letter2:
                j += 1

            i += 1

        return j == len(str2)
