# https://leetcode.com/problems/jump-game-ii/

from typing import List


# Memoization With Dictionary
class Solution:
    def helper(self, ind, nums, dp):
        if ind == len(nums) - 1:
            return 0
        if ind in dp:
            return dp[ind]
        res = float('inf')
        for i in range(ind + 1, min(ind + nums[ind] + 1, len(nums))):
            subres = 1 + self.helper(i, nums, dp)
            res = min(res, subres)
        dp[ind] = res
        return dp[ind]

    def jump(self, nums: List[int]) -> int:
        dp = {}
        return self.helper(0, nums, dp)


# Memoization With List
class Solution:
    def helper(self, ind, nums, dp):
        if ind == len(nums) - 1:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        res = float('inf')
        for i in range(ind + 1, min(ind + nums[ind] + 1, len(nums))):
            subres = 1 + self.helper(i, nums, dp)
            res = min(res, subres)
        dp[ind] = res
        return dp[ind]

    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.helper(0, nums, dp)


# Tabulation DP
class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        dp = [0] * len(nums)
        for ind in range(len(nums) - 2, -1, -1):
            res = float('inf')
            for i in range(ind + 1, min(ind + nums[ind] + 1, len(nums))):
                subres = 1 + dp[i]
                res = min(res, subres)
            dp[ind] = res
        return dp[0]


solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]) == 2)
print(solution.jump([2, 3, 0, 1, 4]) == 2)
print(solution.jump([2, 3, 0, 1]) == 2)
print(solution.jump([2, 3, 1]) == 1)
