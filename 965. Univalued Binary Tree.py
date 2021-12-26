class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        Num = root.val
        Stack = [root]
        while(Stack):
            Curr = Stack.pop()
            if(Curr.val != Num): return False
            if(Curr.right):Stack.append(Curr.right)            
            if(Curr.left):Stack.append(Curr.left)
        return True
