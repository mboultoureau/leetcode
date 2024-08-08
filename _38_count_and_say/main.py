class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        say = self.countAndSay(n - 1)
        result = ""
        count = 1
        last_digit = say[0]
        for letter in say[1:]:
            if last_digit != letter:
                result += str(count) + last_digit
                last_digit = letter
                count = 1
            else:
                count += 1


        result += str(count) + last_digit
        return result