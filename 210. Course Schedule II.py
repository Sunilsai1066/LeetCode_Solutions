class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites:
            AdList = {i:[] for i in range(numCourses)}
            for I,O in prerequisites:
                AdList[O].append(I)
            Stack = []
            Visited = set()
            BFSVisit = [0]*numCourses
            def TopSort(Node,AdList,Visited,BFSVisit):
                Visited.add(Node)
                BFSVisit[Node] = 1
                for i in AdList[Node]:
                    if i not in Visited:
                        if(TopSort(i,AdList,Visited,BFSVisit) == []): return []
                    elif(BFSVisit[i] == 1):
                        return []
                BFSVisit[Node] = 0
                Stack.append(Node)
            for i in AdList.keys():
                if i not in Visited:
                    if(TopSort(i,AdList,Visited,BFSVisit) == []): return []
            return list(reversed(Stack))
        else:
            Ans = []
            for i in range(numCourses-1,-1,-1):
                Ans.append(i)
            return Ans
