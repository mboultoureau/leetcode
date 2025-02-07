class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        balls = defaultdict(int)
        
        nb_colors = 0
        result = [0 for _ in range(len(queries))]

        for i in range(len(queries)):
            ball, color = queries[i]
            colors[balls[ball]] -= 1

            if colors[balls[ball]] == 0:
                nb_colors -= 1

            balls[ball] = color
            colors[color] += 1
            if colors[color] == 1:
                nb_colors += 1

            result[i] = nb_colors

        return result


