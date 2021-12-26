class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        LeftVal = 0
        Stack = [root]
        Flag = 1
        while(Stack):
            StackLen = len(Stack)
            for i in range(StackLen):
                Curr = Stack.pop(0)
                if(Flag): 
                    LeftVal = Curr.val
                    Flag = 0
                if(Curr.left):Stack.append(Curr.left)
                if(Curr.right):Stack.append(Curr.right)
            Flag = 1
        return LeftVal
