class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [[0, 0] for _ in range(n)]
        for t in trust:
            people[t[0] - 1][0] += 1
            people[t[1] - 1][1] += 1

        result = -1
        for i in range(len(people)):
            if people[i] != [0, n - 1]:
                continue

            if result != -1:
                return -1

            result = i + 1

        return result
