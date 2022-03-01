class TrieNode:
    def __init__(self):
        self.NodeLinks = [-1,-1]
        
class Trie:
    def __init__(self):
        self.Root = TrieNode()
        
    def Insert(self,Num):
        Node = self.Root
        for i in range(31,-1,-1):
            Bit = (Num >> i) & 1
            if(Node.NodeLinks[Bit] == -1):
                NewLink = TrieNode()
                Node.NodeLinks[Bit] = NewLink
            Node = Node.NodeLinks[Bit]
                
    def findMax(self,Num):
        SubMax = 0
        Node = self.Root
        for i in range(31,-1,-1):
            Bit = (Num >> i) & 1
            if(Node.NodeLinks[1-Bit] != -1):
                SubMax = SubMax | (1<<i)
                Node = Node.NodeLinks[1-Bit]
            else:
                Node = Node.NodeLinks[Bit]
        return SubMax
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        Tr = Trie()
        for num in nums:
            Tr.Insert(num)
        Max = 0
        for num in nums:
            Max = max(Max,Tr.findMax(num))
        return Max
