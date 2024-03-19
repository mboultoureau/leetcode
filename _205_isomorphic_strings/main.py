class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        matchesFromS = {}
        matchesFromT = {}

        for i in range(len(s)):
            if t[i] not in matchesFromS and s[i] not in matchesFromT:
                matchesFromS[t[i]] = s[i]
                matchesFromT[s[i]] = t[i]
            elif matchesFromS.get(t[i]) != s[i] or matchesFromT.get(s[i]) != t[i]:
                return False

        return True