class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        MaxFar = nums[0]
        MaxYet = nums[0]
        for i in range(1,len(nums)):
            if(nums[i] <= nums[i-1]):
                MaxYet = nums[i]
            else:
                MaxYet += nums[i]
            if(MaxYet > MaxFar):
                MaxFar = MaxYet
        return MaxFar
