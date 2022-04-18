class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def Inorder(root):
            if(root == None):return []
            LV = Inorder(root.left)
            RV = Inorder(root.right)
            return [*LV,root.val,*RV]
        return Inorder(root)[k-1]
