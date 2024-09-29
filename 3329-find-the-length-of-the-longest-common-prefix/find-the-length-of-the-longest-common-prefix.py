class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for n in str(num):
            if n not in node.children:
                node.children[n] = TrieNode()
            node = node.children[n]
    
    def search(self, num):
        node = self.root
        count = 0
        for n in str(num):
            if n not in node.children:
                return count
            node = node.children[n]
            count += 1
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        ans = 0
        for num in arr2:
            ans = max(ans, trie.search(num))
        return ans

        