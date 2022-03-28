"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        Res = []
        if(root == None):return Res
        Stack = [root]
        while(Stack):
            Len = len(Stack)
            SubRes = []
            for Node in range(Len):
                Curr = Stack.pop(0)
                SubRes.append(Curr.val)
                for Child in Curr.children:
                    Stack.append(Child)
            Res.append(SubRes)
        return Res
