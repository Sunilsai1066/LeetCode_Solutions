class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        Arr1 = []
        Arr2 = []
        def FindLeaves(root,Arr):
            if(root == None): return 
            if(root.left == None and root.right == None): Arr.append(root.val)
            FindLeaves(root.left,Arr)
            FindLeaves(root.right,Arr)
        FindLeaves(root1,Arr1)
        FindLeaves(root2,Arr2)
        return Arr1==Arr2
