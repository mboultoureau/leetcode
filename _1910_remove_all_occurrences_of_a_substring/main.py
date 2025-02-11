class Solution:
    def isSubstring(self, stack: list, part: str) -> bool:
        length = len(part)
        for i in range(length):
            if stack[len(stack) - 1 - i] != part[len(part) - 1 - i]:
                return False

        return True


    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])

            # Check if substring
            if len(stack) >= len(part) and self.isSubstring(stack, part):
                for _ in range(len(part)):
                    stack.pop()

        return ''.join(stack)
