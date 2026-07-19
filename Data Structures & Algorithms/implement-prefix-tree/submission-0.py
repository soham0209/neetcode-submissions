class Node:
    def __init__(self, c, is_word=False):
        self.c = c
        self.children = {}
        self.is_word = is_word

class PrefixTree:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = Node(c, False)
            tmp = tmp.children[c]
        tmp.is_word = True 

    def search(self, word: str) -> bool:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                return False
            tmp = tmp.children[c]
        return tmp.is_word

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for c in prefix:
            if c not in tmp.children:
                return False
            tmp = tmp.children[c]
        return True
        
        