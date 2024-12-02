class Solution:
    def startswith(self, word, prefix):
        if len(word) < len(prefix):
            return False

        for i in range(len(prefix)):
            if word[i] != prefix[i]:
                return False

        return True

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i in range(len(words)):
            word = words[i]

            if self.startswith(word, searchWord):
                return i + 1

            # if word.startswith(searchWord):
            #     return i + 1

        return -1