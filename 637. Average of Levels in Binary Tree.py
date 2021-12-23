class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Res = []
        Stack = [root]
        while(Stack):
            Sum = 0
            StackLen = len(Stack)
            for i in range(StackLen):
                Curr = Stack.pop(0)
                Sum += Curr.val
                if(Curr.left):Stack.append(Curr.left)
                if(Curr.right):Stack.append(Curr.right)
            Avg = Sum/StackLen
            Res.append(Avg)
        return Res
