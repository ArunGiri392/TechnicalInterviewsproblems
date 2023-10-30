
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.endofword = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char == ".":
               current_node = current_node.children[char]
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.endofword 



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)