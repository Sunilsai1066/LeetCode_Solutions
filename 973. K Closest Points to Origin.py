class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        MinHeap = []
        for Ind,Point in enumerate(points):
            Dist = (Point[0]**2)+(Point[1]**2)
            heapq.heappush(MinHeap,(Dist,Ind))
        Res = [points[heapq.heappop(MinHeap)[1]] for _ in range(k)]
        return Res
