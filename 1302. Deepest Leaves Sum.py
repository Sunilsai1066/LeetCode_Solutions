class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        Stack = [root]
        Sum = 0
        while(Stack):
            StackLen = len(Stack)
            SubSum = 0
            for i in range(StackLen):
                Curr = Stack.pop(0)
                SubSum += Curr.val
                if(Curr.left):Stack.append(Curr.left)
                if(Curr.right):Stack.append(Curr.right)
            Sum = SubSum
        return Sum
