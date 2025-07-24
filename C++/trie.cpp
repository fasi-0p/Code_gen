#include <iostream>
using namespace std;

struct TrieNode {
    TrieNode* children[26];
    bool isEnd;

    TrieNode() {
        isEnd = false;
        for (int i = 0; i < 26; i++) children[i] = nullptr;
    }
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    // Insert word
    void insert(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx])
                node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    // Search word
    bool search(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx])
                return false;
            node = node->children[idx];
        }
        return node->isEnd;
    }
};

// ✅ Use-case
int main() {
    Trie trie;
    trie.insert("apple");
    trie.insert("app");

    cout << "Search 'apple': " << (trie.search("apple") ? "Found" : "Not Found") << endl;  // Found
    cout << "Search 'ap': " << (trie.search("ap") ? "Found" : "Not Found") << endl;        // Not Found
}
