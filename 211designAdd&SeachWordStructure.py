class Node:
    def __init__(self):
        self.links = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head
        for w in word:
            if w not in curr.links:
                curr.links[w] = Node()
            curr = curr.links[w]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        if word == '.at':
            print(self.head.links)
        return self.trace(self.head, word)

    def trace(self, curr, word):

        if len(word) == 0:
            return curr.isEnd

        w = word[0]

        if w not in curr.links:
            if w == '.':
                for key in curr.links:
                    if self.trace(curr.links[key], word[1:]):
                        return True
            return False
        else:
            return self.trace(curr.links[w], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
