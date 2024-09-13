class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]

        result = []
        for query in queries:
            result.append(prefix[query[1] + 1] ^ prefix[query[0]])

        return result

        # Time Limit Exceeded
        # result = []
        # for query in queries:
        #     answer = arr[query[0]]
        #     for i in range(query[0] + 1, query[1] + 1):
        #         answer ^= arr[i]

        #     result.append(answer)

        # return result