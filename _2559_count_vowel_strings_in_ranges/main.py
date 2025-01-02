class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cumulative = [0 for _ in range(len(words) + 1)]

        for i in range(len(words)):
            increase = 1 if (words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels) else 0
            cumulative[i + 1] = cumulative[i] + increase

        result = [0 for _ in range(len(queries))]
        for i in range(len(queries)):
            l, r = queries[i]
            result[i] = cumulative[r + 1] - cumulative[l]

        return result
