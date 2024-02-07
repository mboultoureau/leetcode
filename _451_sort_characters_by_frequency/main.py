class Solution:
    def frequencySort(self, s: str) -> str:
        values = defaultdict(list)
        letters = defaultdict(int)

        for c in s:
            letters[c] += 1
            if letters[c] - 1 > 0:
                values[letters[c] - 1].remove(c)
            values[letters[c]].append(c)


        result = ""
        for key, val in reversed(values.items()):
            for n in val:
                result += n * key

        return result