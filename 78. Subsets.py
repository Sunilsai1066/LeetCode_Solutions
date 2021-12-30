class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Res = []
        n = len(nums)
        for i in range(2**n):
            SubLis = []
            for j in range(n):
                if(i & (1<<j)):
                    SubLis.append(nums[j])
            Res.append(SubLis)
        return Res
