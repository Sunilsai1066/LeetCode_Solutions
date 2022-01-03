class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def ToGraph(edges):
            graph = {}
            for I,O in edges:
                if I not in graph:
                    graph[I] = [O]
                else:
                    graph[I].append(O)
                if O not in graph:
                    graph[O] = [I]
                else:
                    graph[O].append(I)
            return graph
        graph = ToGraph(dislikes)
        Color = [-1 for _ in range(n+1)]
        def CheckBipartate(graph,Node,Color,PrevColor):
            Color[Node] = PrevColor
            for i in graph[Node]:
                if(Color[i] == -1):
                    if(CheckBipartate(graph,i,Color,1-PrevColor) == False):
                        return False
                elif(Color[i] == PrevColor):
                    return False
            return True
        for i in graph.keys():
            if(Color[i] ==  -1):
                PrevColor = 0
                if(CheckBipartate(graph,i,Color,PrevColor) == False):
                    return False
        return True
