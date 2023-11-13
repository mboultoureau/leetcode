class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        toReplaced = []

        for c in s:
            if c in vowels:
                toReplaced.append(c)

        toReplaced.sort()

        result = ""
        for c in s:
            if c in vowels:
                result += toReplaced[0]
                toReplaced.pop(0)
            else:
                result += c

        return result