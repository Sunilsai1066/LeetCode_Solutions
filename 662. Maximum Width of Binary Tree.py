class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Stack = [(root,0)]
        Max = float("-inf")
        while(Stack):
            StackLen = len(Stack)
            SubRes = []
            for i in range(StackLen):
                CurrNode,CurrVal = Stack.pop(0)
                SubRes.append(CurrVal)
                if(CurrNode.left):Stack.append((CurrNode.left,(2*CurrVal)+1))
                if(CurrNode.right):Stack.append((CurrNode.right,(2*CurrVal)+2))
            MaxVal = SubRes[-1]-SubRes[0]+1
            if(MaxVal > Max):
                Max = MaxVal
        return Max
