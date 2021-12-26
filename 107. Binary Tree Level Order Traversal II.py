class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        Res = []
        if(root == None):return Res
        Stack = [root]
        while(Stack):
            StackLen = len(Stack)
            SubLis = []
            for i in range(StackLen):
                Curr = Stack.pop(0)
                SubLis.append(Curr.val)
                if(Curr.left):Stack.append(Curr.left)
                if(Curr.right):Stack.append(Curr.right)
            Res.insert(0,SubLis)
        return Res
