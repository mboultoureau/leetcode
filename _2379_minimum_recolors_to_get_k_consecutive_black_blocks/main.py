class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blacks = 0
        best = 0
        
        for i in range(k):
            if blocks[i] == "B":
                blacks += 1

        best = blacks

        for i in range(len(blocks) - k):
            if blocks[i] == "B":
                blacks -= 1
            
            if blocks[i + k] == "B":
                blacks += 1

            best = max(best, blacks)

        return k - best if k - best >= 0 else 0 