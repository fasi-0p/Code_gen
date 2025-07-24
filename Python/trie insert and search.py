class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False  # True if this node ends a word

class Trie:
    """
    Trie (Prefix Tree):
    - Used for word insert and prefix/word search.
    - Time Complexity: O(L), where L = word length
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()  # Create new node if not exists
            current = current.children[ch]
        current.end_of_word = True  # Mark end of word

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False  # Char not found
            current = current.children[ch]
        return current.end_of_word  # Return True only if it's a full word

# ✅ Example
trie = Trie()
trie.insert("cat")
trie.insert("car")
print("Search cat:", trie.search("cat"))  # True
print("Search cab:", trie.search("cab"))  # False
