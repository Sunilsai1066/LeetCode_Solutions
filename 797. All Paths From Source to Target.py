class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        Len = len(graph)
        AdjLis = {i:graph[i] for i in range(Len)}
        res = []
        def helper(node, subRes):
            subRes.append(node)
            if(subRes[-1] == Len-1):
                res.append(subRes[:])
                return
            for sub in graph[node]:
                helper(sub, subRes)
                subRes.pop()

        helper(0, [])
        return res
