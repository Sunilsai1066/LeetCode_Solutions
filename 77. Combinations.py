class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        finRes = []
        def helper(ind, subRes):
            if(len(subRes) == k):
                finRes.append(subRes[:])
                return 
            for i in range(ind, n):
                subRes.append(nums[i])
                helper(i+1, subRes)
                subRes.pop()

        helper(0, [])
        return finRes
