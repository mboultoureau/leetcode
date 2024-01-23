class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols = len(board[0])
        rows = len(board)
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def backtracking(i, r, c):
            # Check if visited or invalid
            if visited[r][c] or i >= len(word) or board[r][c] != word[i]:
                return False

            # Check if finished
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True

            # Backtracking
            visited[r][c] = 1
            
            # Left
            if c > 0 and backtracking(i + 1, r, c - 1):
                return True

            # Top
            if r > 0 and backtracking(i + 1, r - 1, c):
                return True

            # Right
            if c < cols - 1 and backtracking(i + 1, r, c + 1):
                return True

            # Bottom
            if r < rows - 1 and backtracking(i + 1, r + 1, c):
                return True

            visited[r][c] = 0
            return False

        for r in range(rows):
            for c in range(cols):
                if backtracking(0, r, c):
                    return True

        return False

