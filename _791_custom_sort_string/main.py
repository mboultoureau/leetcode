class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = ""

        for n in order:
            if n in count:
                result += n * count[n]
                del count[n]

        for key, value in count.items():
            result += key * value

        return result