class Solution:
    def knightDialer(self, n: int) -> int:
        next_moves = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        length = 10
        queue = {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            0: 1
        }
        for i in range(n - 1):
            newQueue = {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
                9: 0,
                0: 0
            }
            
            length = 0
            for key, value in queue.items():
                for next in next_moves[key]:
                    newQueue[next] += value
                    length += value

            queue = newQueue 

        return length % (10 ** 9 + 7)