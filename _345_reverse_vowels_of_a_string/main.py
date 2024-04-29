class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            if self.is_vowel(s[left]) and self.is_vowel(s[right]):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif not self.is_vowel(s[left]):
                left += 1
            elif not self.is_vowel(s[right]):
                right -= 1

        return ''.join(s)

    def is_vowel(self, c):
        return c.lower() in ('a', 'e', 'i', 'o', 'u')