class Node():
    def __init__(self):
        self.child = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.is_word = True

    def r_search(self, curr, sub_string):
        for i,c in enumerate(sub_string):
            if c == ".":
                for child in curr.child.values():
                    if self.r_search(child, sub_string[i+1:]):
                        return True
                return False
            elif c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.is_word
            


    def search(self, word: str) -> bool:
        curr = self.root
        return self.r_search(curr,word)

