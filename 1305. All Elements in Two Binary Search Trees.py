class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        Res = []
        def InOrderIterative(root): 
            Stack = [] 
            Res = [] 
            Curr = root 
            while True:
                if Curr is not None:
                    Stack.append(Curr)
                    Curr = Curr.left
                elif(Stack):
                    Curr = Stack.pop()
                    Res.append(Curr.val)
                    Curr = Curr.right
                else:
                    break
            return Res
        Arr1 = InOrderIterative(root1)
        Arr2 = InOrderIterative(root2)
        i=j=0
        while(i<len(Arr1) and j<len(Arr2)):
            if(Arr1[i] > Arr2[j]):
                Res.append(Arr2[j])
                j += 1
            else:
                Res.append(Arr1[i])
                i += 1
        Res.extend(Arr1[i:])
        Res.extend(Arr2[j:])
        return Res
