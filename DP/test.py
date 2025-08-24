# https://leetcode.com/problems/jump-game-ii/

from typing import List


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
