class DictionaryNode:
    def __init__(self):
        self.val = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = DictionaryNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.val:
                newNode = DictionaryNode()
                current.val[c] = newNode

            current = current.val[c]

        current.end = True


    def search(self, word: str) -> bool:
        queue = deque([self.root])
        c = 0

        while c < len(word):
            length = len(queue)
            while length:
                node = queue.popleft()

                if word[c] == '.':
                    for n in node.val:
                        queue.append(node.val[n])
                elif word[c] in node.val:
                    queue.append(node.val[word[c]])

                length -= 1

            if len(queue) == 0:
                return False

            c += 1

        while queue:
            node = queue.popleft()
            if node.end:
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)