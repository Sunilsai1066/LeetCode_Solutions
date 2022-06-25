class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def helper(ind, xor):
            if(ind >= len(nums)):
                if(res):
                    res.append(res[-1]+xor)
                else:
                    res.append(xor)
                return
            helper(ind+1, xor)
            helper(ind+1, xor^nums[ind])

        helper(0, 0)
        return res[-1]
