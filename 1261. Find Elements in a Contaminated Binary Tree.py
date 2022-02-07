class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.Set = set()
        Stack = [(self.root,0)]
        while(Stack):
            CurrNode,CurrInd = Stack.pop()
            self.Set.add(CurrInd)
            if(CurrNode.left):Stack.append([CurrNode.left,(CurrInd*2)+1])
            if(CurrNode.right):Stack.append([CurrNode.right,(CurrInd*2)+2])
            
    def find(self, target: int) -> bool:
        return target in self.Set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
