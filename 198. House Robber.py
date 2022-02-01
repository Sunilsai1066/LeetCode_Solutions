class Solution:
    def rob(self, nums: List[int]) -> int:
        Len = len(nums)
        Memo = {}
        def Dp(i):
            if(i == 0):
                return nums[i]
            elif(i == 1):
                return max(nums[0],nums[i])
            if i not in Memo:
                Memo[i] = max(Dp(i-1),Dp(i-2)+nums[i])
            return Memo[i]
        return Dp(Len-1)
