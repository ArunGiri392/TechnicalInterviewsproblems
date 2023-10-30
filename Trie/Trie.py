# Trie implementation in python.

class TrieNode:
    def __init__(self):
        # pointer array for child nodes for each node.
        self.childNode = [None] * 26
        self.wordCount = 0
    
def insert_key(root,key):

    # initializing the currentNode pointer with the root.
    currentNode  = root

    # iterate across the string.
    for c in key:
        # check if the node exist for the current character in the Trie
        if currentNode.childNode[ord(c) - ord("a")] == None:
            # then make a new node.
            newNode = TrieNode()
            currentNode.childNode[ord(c) - ord("a")] = newNode

        # move current node pointer to the 
        currentNode = currentNode.childNode[ord(c) - ord("a")]
        # Increment the wordEndCount for the last currentNode 
# pointer this implies that there is a string ending at currentNode. 
    currentNode.wordCount += 1
        
def search(root,key):
    print("search called")
    currentNode = root
    for c in key:
        if currentNode.childNode[ord(c) - ord("a")] == None:
            return False
        currentNode = currentNode.childNode[ord(c) - ord("a")]
    if currentNode.wordCount > 0:
        return True
    return False

root = TrieNode()

# Stores the strings that we want to insert in the Trie 
input_strings = ["and", "ant", "do", "geek", "dad", "ball"] 

 # number of insert operations in the Trie 
n = len(input_strings) 

for i in range(n): 
    insert_key(root, input_strings[i]) 

# Stores the strings that we want to search in the Trie 
search_query_strings = ["do", "geek", "bat"] 
  
# number of search operations in the Trie 
search_queries = len(search_query_strings) 

for i in range(search_queries): 
    print("Query String:", search_query_strings[i]) 
    if search(root, search_query_strings[i]): 
            # the queryString is present in the Trie 
            print("The query string is present in the Trie") 
    else: 
            # the queryString is not present in the Trie 
            print("The query string is not present in the Trie") 

# Insertion: Inserting a word into a Trie has a time complexity of O(L), where L is the length of the word being inserted. This is because you need to traverse the Trie one character at a time and create new nodes if they don't already exist.

# Search: Searching for a word in a Trie also has a time complexity of O(L), where L is the length of the word you are searching for. This is because you need to traverse the Trie character by character until you either find the word or reach a point where it doesn't exist.

# Trie implementation using a dictionary instead of list.
class TrieNode:
    def __init__(self):
        self.children = {}  # A dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the Trie with an empty root node

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node if the character doesn't exist
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the inserted word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # If the character is not found, the word doesn't exist
            node = node.children[char]
        return node.is_end_of_word  # Return True if the word exists

# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))  # True
print(trie.search("app"))  # True
trie.delete("apple")
print(trie.search("apple"))  # False