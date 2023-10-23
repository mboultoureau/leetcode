class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Solution 2 (with intersection)
        if len(magazine) < len(ransomNote):
            return False

        counterNote = Counter(ransomNote)
        counterMagazine = Counter(magazine)

        return counterNote & counterMagazine == counterNote
        
        # Solution 1
        # ransomNote = list(ransomNote)
        # magazine = list(magazine)

        # if len(magazine) < len(ransomNote):
        #     return False

        # for i in ransomNote:
        #     try:
        #         magazine.remove(i)
        #     except:
        #         return False

        # return True