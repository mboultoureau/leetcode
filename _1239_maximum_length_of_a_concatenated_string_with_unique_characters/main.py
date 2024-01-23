class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLength = 0

        def bst(chars: Set, i: int) -> int:
            previousLength = len(chars)

            for c in arr[i]:
                if c in chars:
                    return previousLength

                chars.add(c)

            maximum = len(chars)
            for j in range(i + 1, len(arr)):
                newChars = chars.copy()
                maximum = max(maximum, bst(newChars, j))

            return maximum

        for i in range(len(arr)):
            maxLength = max(maxLength, bst(set(), i))

        return maxLength