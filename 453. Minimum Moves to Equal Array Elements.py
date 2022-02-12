class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Min = min(nums)
        Res = 0
        for i in nums:
            Res += (i-Min)
        return Res
        #return sum(nums) - len(nums)*min(nums) #1 Line Solution
