class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars = Counter(chars)

        for word in words:
            count = Counter(word)
            isValid = True

            for key, value in count.items():
                if chars[key] < value:
                    isValid = False
                    break

            if isValid:
                result += len(word)

        return result