class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Memo = {}
        def helper(ind, currSum):
            if(ind == len(nums)):
                if(currSum == target):
                    return 1
                return 0
            if((ind, currSum) in Memo):
                return Memo[(ind, currSum)]
            else:
                Memo[(ind, currSum)] = helper(ind+1, currSum-nums[ind]) + helper(ind+1, currSum+nums[ind])
            return Memo[(ind, currSum)]
        return helper(0, 0)
