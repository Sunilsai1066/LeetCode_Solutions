class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        Parent = [i for i in range(len(edges)+1)]
        Rank = [0]*(len(edges)+1)
        Res = []
        def FindParent(Node,Parent):
            if(Node == Parent[Node]):
                return Node
            Parent[Node] = FindParent(Parent[Node],Parent)
            return Parent[Node]

        def Union(I,O,Parent,Rank):
            IParent = FindParent(I,Parent)
            OParent = FindParent(O,Parent)
            if(Rank[IParent] == Rank[OParent]):
                Parent[IParent] = OParent
                Rank[OParent] += 1
            elif(Rank[IParent] < Rank[OParent]):
                Parent[IParent] = OParent
            elif(Rank[OParent] < Rank[IParent]):
                Parent[OParent] = IParent
        
        for I,O in edges:
            IParent = FindParent(I,Parent)
            OParent = FindParent(O,Parent)
            if(IParent == OParent):
                Res.append([I,O])
            Union(IParent,OParent,Parent,Rank)
        return Res[-1]
