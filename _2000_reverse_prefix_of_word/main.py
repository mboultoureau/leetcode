class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Solution 2
        word = list(word)
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break

        if idx == -1:
            return ''.join(word)

        for i in range(0, idx // 2 + 1):
            word[i], word[idx - i] = word[idx - i], word[i]

        return ''.join(word)

        # Solution 1
        # idx = word.find(ch)
        # if idx == -1:
        #     return word

        # return word[idx::-1] + word[idx + 1:]