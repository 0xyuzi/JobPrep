# define a TrieNode

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_children = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        start from root node and check if node's chilad already in
        if not in create a new TrieNone and contitinue
        finally, put the final node with is_child = True
        """
        node = self.root
        for c in word:
            if not node.children.get(c):  
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_children = True
            
    
    def find(self, substring):
        node = self.root
        for c in substring:
            if not node.children.get(c):
                return None
            node = node.children[c]
            
        return node 
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        
        if node != None and node.is_children:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        
        if node != None:
            return True
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)