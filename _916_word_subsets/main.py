class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = [0 for _ in range(26)]
        result = []

        for word in words2:
            letters = Counter(word)
            for c in letters:
                if count[ord(c) - ord('a')] < letters[c]:
                    count[ord(c) - ord('a')] = letters[c]

        for word in words1:
            letters = Counter(word)
            valid = True
            for i in range(26):
                if count[i] > letters[chr(i + ord('a'))]:
                    valid = False
                    break

            if valid:
                result.append(word)

        return result