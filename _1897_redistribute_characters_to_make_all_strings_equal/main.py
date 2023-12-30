class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Solution 2
        letters = Counter("".join(words))
        for value in letters.values():
            if value % len(words) != 0:
                return False

        return True
        
        # Solution 1
        # letters = Counter()
        # for word in words:
        #     letters += Counter(word)

        # for value in letters.values():
        #     if value % len(words) != 0:
        #         return False

        # return True