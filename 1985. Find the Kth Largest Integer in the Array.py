class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        MinHeap = []
        heapify(MinHeap)
        for num in nums:
            if(len(MinHeap) < k):
                heappush(MinHeap,int(num))
            elif(MinHeap[0] < int(num)):
                heappushpop(MinHeap,int(num))
        return str(MinHeap[0])
