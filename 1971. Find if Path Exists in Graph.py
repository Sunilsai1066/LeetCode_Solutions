class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if((start==end) or [start,end] in edges):return True
        AdList = {}
        for edge in edges:
            if(edge[0] not in AdList):
                AdList[edge[0]] = [edge[1]]
            else:
                AdList[edge[0]].append(edge[1])
            if(edge[1] not in AdList):
                AdList[edge[1]] = [edge[0]]
            else:
                AdList[edge[1]].append(edge[0])
        Visit = [False]*n
        Stack = [start]
        while(Stack):
            Curr = Stack.pop()
            if(Curr == end):return True
            elif(Curr in AdList and not Visit[Curr]):
                Stack.extend(AdList[Curr])
            Visit[Curr] = True
        return False
