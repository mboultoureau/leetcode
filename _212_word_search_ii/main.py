class TrieNode:
    def __init__(self):
        self.val = {}
        self.count = 0
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        NB_ROWS = len(board)
        NB_COLS = len(board[0])

        self.root = TrieNode()
        for word in words:
            self.addWord(word)

        result = set()
        visited = [[False for _ in range(NB_COLS)] for _ in range(NB_ROWS)]

        def backtracking(r, c, node, word):
            if visited[r][c] == True or board[r][c] not in node.val or node.val[board[r][c]].count == 0:
                return

            node = node.val[board[r][c]]
            visited[r][c] = True
            word += board[r][c]

            if node.end:
                result.add(word)
                node.end = False
                self.removeWord(word)

            # Left
            if c > 0 and backtracking(r, c - 1, node, word):
                return True

            # Top
            if r > 0 and backtracking(r - 1, c, node, word):
                return True

            # Right
            if c < NB_COLS - 1 and backtracking(r, c + 1, node, word):
                return True

            # Bottom
            if r < NB_ROWS - 1 and backtracking(r + 1, c, node, word):
                return True

            visited[r][c] = False

            return False

        for r in range(NB_ROWS):
            for c in range(NB_COLS):
                backtracking(r, c, self.root, "")

        return result

    def addWord(self, word):
        current = self.root
        for c in word:
            if c not in current.val:
                newNode = TrieNode()
                current.val[c] = newNode

            current.val[c].count += 1
            current = current.val[c]
        
        current.end = True

    def removeWord(self, word):
        current = self.root
        for c in word:
            current.val[c].count -= 1
            current = current.val[c]