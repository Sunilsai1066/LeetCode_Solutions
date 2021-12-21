class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root == None or root == p or root == q):return root
        LeftVal = self.lowestCommonAncestor(root.left,p,q)
        RightVal = self.lowestCommonAncestor(root.right,p,q)
        if(LeftVal == None):return RightVal
        elif(RightVal == None): return LeftVal
        else: return root
