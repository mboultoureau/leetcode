class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Solution 4
        result = 0
        for _ in range(32):
            if start & 1 != goal & 1:
                result += 1

            start >>= 1
            goal >>= 1

        return result

        # Solution 3
        # diff = start ^ goal
        # result = 0
        # for _ in range(32):
        #     if diff & 1 == 1:
        #         result += 1

        #     diff >>= 1

        # return result

        # Solution 2
        # diff = start ^ goal
        # return bin(diff).count('1')

        
        # Solution 1
        # start = bin(start)[2:].zfill(32)
        # goal = bin(goal)[2:].zfill(32)
        # result = 0

        # for i in range(len(goal)):
        #     if goal[i] != start[i]:
        #         result += 1

        # return result