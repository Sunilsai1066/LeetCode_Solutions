class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.Sum = 0
        def LeftSum(root):
            if(root == None):return 0
            if(root.left):
                if(root.left.left == None and root.left.right == None):
                    self.Sum += root.left.val
                else:
                    LeftVal = LeftSum(root.left)
            RightVal = LeftSum(root.right)
        LeftSum(root)
        return self.Sum
