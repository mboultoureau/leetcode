class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        length = len(s)

        for letter in count:
            length -= (count[letter] - 1) // 2 * 2

        return length