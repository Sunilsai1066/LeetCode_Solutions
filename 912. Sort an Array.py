#HeapSort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        Res = []
        while(nums):
            Res.append(heappop(nums))
        return Res
