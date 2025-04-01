class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        points = [0] * len(questions)

        for i in range(len(questions) - 1, -1, -1):
            point, brainpower = questions[i]
            next_points = points[i + brainpower + 1] if i + brainpower + 1 < len(questions) else 0
            points[i] = max(points[i + 1] if i + 1 < len(questions) else 0, point + next_points)

        return points[0]


        # @lru_cache(None)
        # def backtracking(i):
        #     if i >= len(questions):
        #         return 0

        #     point, brainpower = questions[i]
        #     return max(
        #         backtracking(i + 1),
        #         point + backtracking(i + brainpower + 1)
        #     )

        # return backtracking(0)