class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxVal = 0
        for i in nums:
            maxVal |= i
        def helper(ind, orVal):
            if(ind == len(nums)):
                if(orVal == maxVal):
                    return 1
                return 0
            return helper(ind+1, orVal) + helper(ind+1, orVal|nums[ind])

        return helper(0, 0)
