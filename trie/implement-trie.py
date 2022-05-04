class TrieNode:
    def __init__(self):
        self.children = [False]*26
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()    
            current = current.children[idx]
       
        current.isEnd = True
    def search(self, word: str, prefix = False) -> bool:
        current = self.root
        for c in word:
            idx = ord(c) - ord('a')
            
            if current.children[idx]:
                
                current = current.children[idx]
            else:
               
                return False
           
        return (current.isEnd or prefix)
        
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix,True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
