class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        Sol = 0
        Stack = [(original,cloned)]
        while(Stack):
            Org,Clone = Stack.pop(0)
            if(Org.val == target.val):
                return Clone
            if(Org.left):Stack.append((Org.left,Clone.left))
            if(Org.right):Stack.append((Org.right,Clone.right))
