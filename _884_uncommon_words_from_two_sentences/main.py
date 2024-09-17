class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = Counter((s1 + ' ' + s2).split(' '))
        return [word for (word, count) in words.items() if count == 1]