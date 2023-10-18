class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for c in s:
            if c in matching:
                stack.append(matching[c])
            elif len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                return False

        return len(stack) == 0