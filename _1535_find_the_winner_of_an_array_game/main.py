class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # Solution 2: faster
        if k > len(arr):
            return max(arr)

        winner = max(arr[0], arr[1])
        winner_count = 1
        i = 2 % len(arr)

        while winner_count != k:
            if arr[i] > winner:
                winner_count = 1
                winner = arr[i]
            else:
                winner_count += 1

            i = (i + 1) % len(arr)

        return winner

        # Solution 1: naive solution
        # if k > len(arr):
        #     return max(arr)

        # win_count = 0
        # while win_count != k:
        #     if arr[0] > arr[1]:
        #         win_count += 1
        #         loser = arr[1]
        #         arr.pop(1)
        #         arr.append(loser)
        #     else:
        #         win_count = 1
        #         loser = arr[0]
        #         arr.pop(0)
        #         arr.append(loser)

        # return arr[0]