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
        
    def Replace(self,Word):
        Node = self.Root
        Sub = ""
        for ch in Word:
            if(Node.End):
                break
            elif(ch not in Node.NodeLinks):
                return Word
            else:
                Sub += ch
                Node = Node.NodeLinks[ch]
        if(Node.End):
            return Sub
        return Word                  
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Tr = Trie()
        Res = []
        for word in dictionary:
            Tr.Insert(word)
        for word in sentence.split(" "):
            Res.append(Tr.Replace(word))
        return " ".join(Res)
