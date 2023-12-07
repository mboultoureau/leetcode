class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = str(num)
        for i in range(len(num) - 1, -1, -1):
            if num[i] == "1" or num[i] == "3" or num[i] == "5" or num[i] == "7" or num[i] == "9":
                return num[0:i + 1]

        return ""