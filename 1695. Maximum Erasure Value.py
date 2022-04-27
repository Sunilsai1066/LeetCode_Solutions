class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        SeenSet = set([nums[0]])
        SumYet = nums[0]
        MaxErasure = SumYet
        numsLen = len(nums)
        StartInd = 0
        Ind = 1
        while(Ind < numsLen):
            if(nums[Ind] not in SeenSet):
                SumYet += nums[Ind]
                SeenSet.add(nums[Ind])
                Ind += 1
            else:
                SumYet -= nums[StartInd]
                SeenSet.remove(nums[StartInd])
                StartInd += 1
            if(SumYet > MaxErasure):
                MaxErasure = SumYet
        return MaxErasure
        
        
