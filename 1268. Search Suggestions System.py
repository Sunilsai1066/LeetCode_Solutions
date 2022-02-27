class TrNode:
    def __init__(self):
        self.NodeLinks = {}
        self.Lis = []
        self.Count = 0

class Trie:
    def __init__(self):
        self.Root = TrNode()
        
    def Insert(self,Word):
        Node = self.Root
        for ch in Word:
            if(ch not in Node.NodeLinks):
                Node.NodeLinks[ch] = TrNode()
            Node = Node.NodeLinks[ch]
            if(Node.Count < 3):
                Node.Lis.append(Word)
                Node.Count += 1
    
    def FindLis(self,Word):
        Node = self.Root
        for ch in Word:
            if(ch not in Node.NodeLinks):
                return []
            Node = Node.NodeLinks[ch]
        return Node.Lis
                  
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        Tr = Trie()
        for product in products:
            Tr.Insert(product)
        ResLis = []
        Curr = ""
        for ch in searchWord:
            Curr += ch
            ResLis.append(Tr.FindLis(Curr))
        return ResLis
