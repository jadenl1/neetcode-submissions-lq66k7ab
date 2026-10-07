class PrefixTree:

    class TrieNode:
        def __init__(self, isEndOfWord, children):
            self.isEndOfWord = isEndOfWord
            self.children = children

    def __init__(self):
        self.root = self.TrieNode(False, {})

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        while i < len(word):
            char = word[i]
            if char not in curr.children:
                curr.children[char] = self.TrieNode(False, {})
            curr = curr.children[char]
            i += 1

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        i = 0
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        return i == len(word) and curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        i = 0
        while i < len(prefix) and prefix[i] in curr.children:
            curr = curr.children[prefix[i]]
            i += 1
        
        return i == len(prefix)
        