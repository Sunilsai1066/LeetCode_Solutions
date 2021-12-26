class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):return []
        Res = []
        Stack = [root]
        while(Stack):
            Max = float("-inf")
            StackLen = len(Stack)
            for i in range(StackLen):
                Curr = Stack.pop(0)
                if(Curr.val > Max):Max = Curr.val
                if(Curr.left):Stack.append(Curr.left)
                if(Curr.right):Stack.append(Curr.right)
            Res.append(Max)
        return Res
