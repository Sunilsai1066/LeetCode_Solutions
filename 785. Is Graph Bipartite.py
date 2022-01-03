class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def List(graph):
            AdjList = {}
            for i in range(len(graph)):
                AdjList[i] = graph[i]
            return AdjList
        AdjList = List(graph)
        Color = [-1 for _ in range(len(AdjList.keys()))]
        def CheckBipartate(Node,Color):
            Queue = [Node]
            Color[Node] = 0
            PrevColor = 0
            while(Queue):
                Curr = Queue.pop(0)
                if(Color[Curr] == 0):
                    PrevColor = 1
                else:
                    PrevColor = 0
                for i in AdjList[Curr]:
                    if(Color[i] == -1):
                        Queue.append(i)
                        Color[i] = PrevColor
                    elif(Color[i] == Color[Curr]):
                        return False
            return True
        for i in AdjList.keys():
            if(Color[i] ==  -1):
                if(CheckBipartate(i,Color) == False):
                    return False
        return True
