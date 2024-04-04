class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return []

        result = []

        def backtracking(i, current):
            if i >= len(digits):
                result.append(''.join(current))
                return

            for letter in mapping[digits[i]]:
                current.append(letter)
                backtracking(i + 1, current)
                current.pop()

        backtracking(0, [])

        return result