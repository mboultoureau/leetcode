class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        previous = -1
        result = []
        for i in range(len(groups)):
            if previous != groups[i]:
                previous = groups[i]
                result.append(words[i])

        return result