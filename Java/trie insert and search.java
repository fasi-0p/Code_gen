public class Trie {

    // Trie node
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];  // For 'a' to 'z'
        boolean isEndOfWord;  // Marks end of a valid word
    }

    static class TrieImpl {
        TrieNode root = new TrieNode();

        // Insert word into trie
        public void insert(String word) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                int index = c - 'a';

                // Create a new node if path doesn't exist
                if (node.children[index] == null)
                    node.children[index] = new TrieNode();

                node = node.children[index];  // Move to next node
            }
            node.isEndOfWord = true;  // Mark end of word
        }

        // Search if word exists in trie
        public boolean search(String word) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                int index = c - 'a';

                if (node.children[index] == null)
                    return false;

                node = node.children[index];
            }
            return node.isEndOfWord;  // Return true if end is marked
        }
    }

    public static void main(String[] args) {
        TrieImpl trie = new TrieImpl();

        trie.insert("cat");
        trie.insert("car");
        trie.insert("cart");

        System.out.println("Search cat: " + trie.search("cat"));   // true
        System.out.println("Search cap: " + trie.search("cap"));   // false
    }
}
