class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count = Counter(nums)
        MinHeap = []
        for K,V in Count.items():
            if(len(MinHeap) < k):
                heappush(MinHeap,(V,K))
            else:
                heappushpop(MinHeap,(V,K))
        Res = [i[1] for i in MinHeap]
        return Res
