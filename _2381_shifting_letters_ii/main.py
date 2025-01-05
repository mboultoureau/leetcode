class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for _ in range(len(s) + 1)]
        for start, end, direction in shifts:
            direction = 1 if direction == 1 else -1
            prefix[end + 1] += direction
            prefix[start] += -direction

        s = list(s)
        diff = prefix[len(s)]
        for i in range(len(s) - 1, -1, -1):
            s[i] = chr((ord(s[i]) - ord('a') + diff) % 26 + ord('a'))
            diff += prefix[i]

        return ''.join(s)

        # TOO SLOW
        # s = list(s)

        # for start, end, direction in shifts:
        #     for i in range(start, end + 1):
        #         direction = 1 if direction == 1 else -1
        #         s[i] = chr((ord(s[i]) - ord('a') + direction) % 26 + ord('a'))

        # return ''.join(s)