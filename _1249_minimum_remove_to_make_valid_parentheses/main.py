class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []

        # Remove extra closing parentheses
        count = 0
        for c in  s:
            if c == '(':
                count += 1
            elif c == ')':
                if count <= 0:
                    continue
                else:
                    count -= 1

            result.append(c)

        # Remove extra opening parentheses
        count = 0
        for i in range(len(result) - 1, -1, -1):
            if result[i] == ')':
                count += 1
            elif result[i] == '(':
                if count <= 0:
                    result.pop(i)
                else:
                    count -= 1

        return "".join(result)