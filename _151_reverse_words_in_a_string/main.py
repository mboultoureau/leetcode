class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        left = len(s) - 1
        right = len(s) - 1

        while left >= 0:
            if s[left] != ' ':
                left -= 1
            elif left == right:
                left -= 1
                right -= 1
            else:
                stack.append(s[left + 1:right + 1])
                right = left - 1
                left -= 1

        if left != right:
            stack.append(s[left + 1:right + 1])

        return ' '.join(stack)