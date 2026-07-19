class Node:
    def __init__(self, c, is_word=False):
        self.c = c
        self.children = {}
        self.is_word = is_word

class WordDictionary:

    def __init__(self):
        self.root = Node("") 
        

    def addWord(self, word: str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = Node(c)
            tmp = tmp.children[c]
        tmp.is_word = True

    def search(self, word: str) -> bool:
        tmp = self.root
        return self.search_helper(tmp, word, 0)
    
    def search_helper(self, trie_node, word, i):
        if i == len(word):
            return trie_node.is_word
        if word[i] in trie_node.children:
            c = word[i]
            return self.search_helper(trie_node.children[c], word, i+1)
        elif word[i] == ".":
            for k, v in trie_node.children.items():
                ans = self.search_helper(v, word, i+1)
                if ans:
                    return True
            return False
        return False



        
