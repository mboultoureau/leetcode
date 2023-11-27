class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        previous = pref[0]
        for i in range(1, len(pref)):
            tmp = pref[i]
            pref[i] = previous ^ pref[i]
            previous = tmp

        return pref