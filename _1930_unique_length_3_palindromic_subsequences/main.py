class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters_min = [-1] * 26
        letters_max = [-1] * 26
        count = 0

        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            if letters_min[c] == -1:
                letters_min[c] = i

            letters_max[c] = i

        for i in range(len(letters_min)):
            if letters_min[i] != -1 and letters_max[i] > letters_min[i] + 1:
                count += len(set(s[letters_min[i] + 1:letters_max[i]]))

        return count

        # Time limit exceeded
        # sequences = set()
        # letters = set()

        # for i in range(len(s) - 2):
        #     if s[i] in letters:
        #         continue

        #     letters.add(s[i])
        #     for j in range(i + 2, len(s)):
        #         if s[i] == s[j]:
        #             for k in range(i + 1, j):
        #                 sequences.add(s[i] + s[k] + s[j])

        # return len(sequences)


        # Time limit exceeded
        # sequences = set()

        # for i in range(len(s) - 2):
        #     for j in range(i + 2, len(s)):
        #         if s[i] == s[j]:
        #             for k in range(i + 1, j):
        #                 sequences.add(s[i] + s[k] + s[j])

        # return len(sequences)


        # Time limit exceeded
        # sequences = set()

        # for i in range(len(s)):
        #     for j in range(i + 1, len(s)):
        #         for k in range(j + 1, len(s)):
        #             if s[i] == s[k]:
        #                 sequences.add(s[i] + s[j] + s[k])

        # return len(sequences)