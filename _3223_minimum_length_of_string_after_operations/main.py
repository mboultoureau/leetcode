class Solution:
    def minimumLength(self, s: str) -> int:
        # Solution 1
        count = Counter(s)
        total = 0

        for c in count:
            total += ((count[c] + 1) % 2) + 1

        return total

        # Solution 2
        # count = Counter(s)
        # length = len(s)

        # for letter in count:
        #     length -= (count[letter] - 1) // 2 * 2

        # return length