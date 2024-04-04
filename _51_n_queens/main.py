class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        columns = set()
        diagonals1 = set()
        diagonals2 = set()
        grid = [['.' for _ in range(n)] for _ in range(n)]

        def backtracking(y):
            if y == n:
                answer = [''.join(row) for row in grid]
                result.append(answer)
                return

            for x in range(n):
                d1 = y - x
                d2 = y + x

                if x in columns or d1 in diagonals1 or d2 in diagonals2:
                    continue

                grid[y][x] = 'Q'
                columns.add(x)
                diagonals1.add(d1)
                diagonals2.add(d2)

                backtracking(y + 1)

                grid[y][x] = '.'
                columns.remove(x)
                diagonals1.remove(d1)
                diagonals2.remove(d2)

        backtracking(0)

        return result


        # Solution 1
        # result = []
        # columns = set()
        # rows = set()
        # diagonals1 = set()
        # diagonals2 = set()
        # grid = [[False for _ in range(n)] for _ in range(n)]

        # def backtracking(i, count):
        #     if count == n:
        #         answer = []
        #         for row in grid:
        #             line = ''
        #             for cell in row:
        #                 line += 'Q' if cell else '.'
        #             answer.append(line)
        #         result.append(answer)
        #         return

        #     if i >= n * n:
        #         return

        #     y = i // n
        #     x = i % n
        #     d1 = y - x
        #     d2 = y + x

        #     if y in columns or x in rows or d1 in diagonals1 or d2 in diagonals2:
        #         backtracking(i + 1, count)
        #         return

        #     grid[y][x] = True
        #     columns.add(y)
        #     rows.add(x)
        #     diagonals1.add(d1)
        #     diagonals2.add(d2)

        #     backtracking(i + 1, count + 1)

        #     grid[y][x] = False
        #     columns.remove(y)
        #     rows.remove(x)
        #     diagonals1.remove(d1)
        #     diagonals2.remove(d2)
        #     backtracking(i + 1, count)

        # backtracking(0, 0)

        # return result
