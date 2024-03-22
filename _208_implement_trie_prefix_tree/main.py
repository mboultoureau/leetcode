class TrieNode:
    def __init__(self):
        self.end = False
        self.val = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            c = ord(c) - ord('a')

            if c not in current.val:
                newNode = TrieNode()
                current.val[c] = newNode

            current = current.val[c]

        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            c = ord(c) - ord('a')
            if c not in current.val:
                return False

            current = current.val[c]

        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            c = ord(c) - ord('a')
            if c not in current.val:
                return False

            current = current.val[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)