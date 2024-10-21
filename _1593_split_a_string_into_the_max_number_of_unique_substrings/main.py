class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtracking(index: int, visited: set) -> int:
            if index == len(s):
                return 0

            result = 0
            for i in range(index, len(s)):
                substring = s[index:i+1]
                
                if substring in visited:
                    continue

                visited.add(substring)
                result = max(result, 1 + backtracking(i + 1, visited))
                visited.remove(substring)

            return result

        return backtracking(0, set())