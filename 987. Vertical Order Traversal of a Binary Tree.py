class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        Stack = [(root,0)]
        Res = []
        Level = 0
        while(len(Stack) > 0):
            Len = len(Stack)
            for i in range(Len):
                CurrNode,CurrValue = Stack.pop(0)
                Res.append((CurrNode.val,CurrValue,Level))
                if(CurrNode.left):Stack.append((CurrNode.left,CurrValue-1))
                if(CurrNode.right):Stack.append((CurrNode.right,CurrValue+1))
            Level += 1
        Res.sort(key = lambda x:(x[1],x[2],x[0]))
        ResDic = {}
        for i in Res:
            if i[1] not in ResDic:
                ResDic[i[1]] = [i[0]]
            else:
                ResDic[i[1]].append(i[0])
        FinRes = []
        for K,V in ResDic.items():
            FinRes.append(V)
        return FinRes
