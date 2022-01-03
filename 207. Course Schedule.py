class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdList = {i:[] for i in range(numCourses)}
        for I,O in prerequisites:
            AdList[O].append(I)
        Visited = [0]*numCourses
        BFSVisit = [0]*numCourses
        def Cycle(Node,AdList,Visited,BFSVisit):
            Visited[Node] = 1
            BFSVisit[Node] = 1
            for i in AdList[Node]:
                if(Visited[i] == 0):
                    if(Cycle(i,AdList,Visited,BFSVisit) == True): return True
                elif(BFSVisit[i] == 1):
                    return True
            BFSVisit[Node] = 0
        for i in AdList.keys():
            if(Visited[i] == 0):
                if(Cycle(i,AdList,Visited,BFSVisit) == True):
                    return False
        return True
