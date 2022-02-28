class TrieNode:
    def __init__(self):
        self.NodeLinks = {}
        self.End = False
    
class Trie:
    def __init__(self,Word):
        self.Root = TrieNode()
        self.Word = Word
        
    def Insert(self):
        Node = self.Root
        for ch in self.Word:
            NewLink = TrieNode()
            Node.NodeLinks[ch] = NewLink
            Node = Node.NodeLinks[ch]
            
    def CheckSub(self,Sub):
        SubLen,WLen = len(Sub),len(self.Word)
        Ind,NodeInd,Count = 0,0,0
        Node = self.Root
        while(Ind < SubLen and NodeInd < WLen):
            if(Sub[Ind] in Node.NodeLinks):
                Count += 1
                Node = Node.NodeLinks[Sub[Ind]]
                Ind += 1
                NodeInd += 1
            else:
                Node = Node.NodeLinks[self.Word[NodeInd]]
                NodeInd += 1
        return 1 if(Count == SubLen) else 0
    
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        Tr = Trie(s)
        Tr.Insert()
        Count = 0
        Memo = {}
        for word in words:
            if(word in Memo):
                Count += Memo[word]
            else:
                Val = Tr.CheckSub(word)
                Memo[word] = Val
                Count += Val
        return Count
