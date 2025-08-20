# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        maxi = nums[0]
        for i in range(1, len(nums)):
            if maxi < i:
                return False
            maxi = max(maxi, i + nums[i])
        return True


solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]) is True)
print(solution.canJump([3, 2, 1, 0, 4]) is False)
print(solution.canJump([5, 3, 2, 1, 0]) is True)
