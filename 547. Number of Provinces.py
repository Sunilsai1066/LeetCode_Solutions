class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        Len = len(isConnected)
        Parent = [i for i in range(Len)]
        Rank = [1 for i in range(Len)]
        def Find(X):
            if(X != Parent[X]):
                Parent[X] = Find(Parent[X])
            return Parent[X]
        def Union(A,B):
            ParentA = Find(A)
            ParentB = Find(B)
            if(ParentA != ParentB):
                if(Rank[ParentA] > Rank[ParentB]):
                    Parent[ParentB] = ParentA
                elif(Rank[ParentA] < Rank[ParentB]):
                    Parent[ParentA] = ParentB
                else:
                    Parent[ParentA] = ParentB
        for i in range(Len):
            for j in range(Len):
                if(i != j and isConnected[i][j] == 1):
                    Union(i,j)
        for i in range(Len):
            Parent[i] = Find(i)
        return len(set(Parent))
