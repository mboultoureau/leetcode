class Solution:
    def isAlphanumeric(self, c) -> bool:
        if c >= 'a' and c <= 'z':
            return True
        if c >= 'A' and c <= 'Z':
            return True
        if c >= '0' and c <= '9':
            return True

        return False

    def getChar(self, c):
        if c >= 'A' and c <= 'Z':
            return chr(ord(c) - ord('A') + ord('a'))

        return c
    
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            
            while right > left and not self.isAlphanumeric(s[right]):
                right -= 1

            if self.getChar(s[left]) != self.getChar(s[right]):
                return False

            left += 1
            right -= 1

        return True