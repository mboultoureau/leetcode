class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        nbRounds = min(x, y // 4)
        if nbRounds % 2 == 0:
            return "Bob"
        else:
            return "Alice"