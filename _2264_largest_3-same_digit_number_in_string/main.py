class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maximum = ""
        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] and num[i - 1] == num[i] and num[i] > maximum:
                if num[i] == "9":
                    return "999"
                else:
                    maximum = num[i]

        return maximum + maximum + maximum