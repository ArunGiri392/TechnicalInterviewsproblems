class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endofword = True
        

class Solution:
     def longestCommonPrefix(self, strs: List[str]) -> str:
         if not string:
             return ""
         trie = Trie()
         for word in strs:
             trie.insert(word)
        
         result = ""
         current = trie.root
         while ( len(current.children) == 1 and current.endofword != True):
              character = list(current.children.keys())[0]
              result += character
              current = current.children[character]
         return result



        
# a = Trie()
# strs = ["flower","flow","flight"]
# a.longestCommonPrefix(strs)
        