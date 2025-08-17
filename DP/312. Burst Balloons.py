from typing import List


class Solution:
    def helper(self, i, j, nums, dp):
        if i > j:
            return 0
        res = float("-inf")
        if (i, j) in dp:
            return dp[(i, j)]
        for k in range(i, j + 1):
            subres = ((nums[k] * nums[i - 1] * nums[j + 1]) +
                      self.helper(i, k - 1, nums, dp) +
                      self.helper(k + 1, j, nums, dp))
            res = max(res, subres)
        dp[(i, j)] = res
        return dp[(i, j)]

    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        dp = {}
        return self.helper(1, len(nums) - 2, nums, dp)


solution = Solution()
print(solution.maxCoins([3, 1, 5, 8]) == 167)
print(solution.maxCoins([1, 5]) == 10)
