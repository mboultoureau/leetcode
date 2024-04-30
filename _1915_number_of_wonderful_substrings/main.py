class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0 for _ in range(2**10)]
        result = 0
        prefix = 0

        count[prefix] = 1
        
        for c in word:
            idx = ord(c) - ord('a')
            prefix ^= 1 << idx
            # If we meet same configuration, add
            result += count[prefix]

            # Check if one odd
            for i in range(10):
                result += count[prefix ^ (1 << i)]

            count[prefix] += 1

        return result 