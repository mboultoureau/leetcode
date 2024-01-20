class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # With NeetCode video
        result = 0
        arr.insert(0, -math.inf)
        arr.append(-math.inf)
        queue = deque([])

        for i in range(len(arr)):
            while queue and arr[i] < queue[-1][1]:
                j, val = queue.pop()
                if queue:
                    left = j - queue[-1][0]
                else:
                    left = j + 1
                right = i - j
                result += (val * left * right)
            queue.append((i, arr[i]))

        return  result % (10 ** 9 + 7)



        # Too slow......
        # result = 0
        # for length in range(1, len(arr) + 1):
        #     for i in range(0, len(arr) - length + 1):
        #         result += min(arr[i:i + length])

        # return result % (10 ** 9 + 7)