class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        self.Flag = False

class Trie:
    def __init__(self):
        self.Main = Node()
        self.Root = self.Main
        self.RtCopy = self.Root

    def insert(self, Word: str) -> None:
        self.Root = self.Main
        self.RtCopy = self.Root
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] == 0):
                self.NextLink = Node()
                self.Root.NodeLinks[ord(letter)-97] = self.NextLink
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                self.Root = self.Root.NodeLinks[ord(letter)-97]
        self.Root.Flag = True

    def search(self, Word: str) -> bool:
        self.Root = self.Main
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return False
        return self.Root.Flag == True
        
    def startsWith(self, Word: str) -> bool:
        self.Root = self.Main
        SWith = True
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                SWith = False
                break
        return SWith
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
