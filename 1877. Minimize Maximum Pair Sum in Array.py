class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        Start,End = 0,len(nums)-1
        Res = 0
        while(Start < End):
            Res = max(Res,nums[Start]+nums[End])
            Start += 1
            End -= 1
        return Res
