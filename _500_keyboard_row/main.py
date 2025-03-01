class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set(list('qwertyuiop')),
            set(list('asdfghjkl')),
            set(list('zxcvbnm'))
        ]

        result = []

        for word in words:
            r = 0
            if word[0].lower() in rows[1]:
                r = 1
            elif word[0].lower() in rows[2]:
                r = 2

            valid = True
            for c in word[1:]:
                if c.lower() not in rows[r]:
                    valid = False
                    break

            if valid:
                result.append(word)

        return result