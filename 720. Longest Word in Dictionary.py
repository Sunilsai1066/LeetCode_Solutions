class TrieNode:
    def __init__(self):
        self.NodeLinks = {}
        self.End = False
        
class Trie:
    def __init__(self):
        self.Root = TrieNode()
        
    def Insert(self,Word):
        Node = self.Root
        for ch in Word:
            if(ch not in Node.NodeLinks):
                NewLink = TrieNode()
                Node.NodeLinks[ch] = NewLink
            Node = Node.NodeLinks[ch]
        Node.End = True
    
    def longWord(self,word):
        Node = self.Root
        for ch in word:
            Node = Node.NodeLinks[ch]
            if(Node.End == False):
                return Node.End
        return True
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        Tr = Trie()
        for word in words:
            Tr.Insert(word)
        Res,Max = "",0
        for word in words:
            if(Tr.longWord(word)):
                if(len(word) > Max):
                    Res,Max = word,len(word)
                elif(len(word) == Max and word < Res):
                    Res = word
        return Res
