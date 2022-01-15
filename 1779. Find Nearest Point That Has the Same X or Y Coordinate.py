class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ManDist = lambda a,b : abs(a-x)+abs(b-y)
        MinHeap = []
        for Ind,(St,End) in enumerate(points):
            if(St == x or End == y):
                Dist = ManDist(St,End)
                heappush(MinHeap,(Dist,Ind))
        return heappop(MinHeap)[1] if MinHeap else -1
