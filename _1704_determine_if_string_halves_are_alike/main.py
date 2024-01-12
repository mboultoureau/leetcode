class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        nbVowels = 0
        vowels = set('aeiouAEIOU')

        for i in range(len(s) // 2):
            if s[i] in vowels:
                nbVowels += 1

        for i in range(len(s) // 2, len(s)):
            if s[i] in vowels:
                nbVowels -= 1

        return nbVowels == 0