from typing import List


class Solution:
    def helper(self, i, j, nums, dp):
        if i == j:
            dp[i][j] = 0
            return dp[i][j]
        res = float("inf")
        if dp[i][j] != -1:
            return dp[i][j]
        for k in range(i, j):
            subres = (nums[k] * nums[i - 1] * nums[j]) + self.helper(i, k, nums, dp) + self.helper(k + 1, j, nums, dp)
            res = min(res, subres)
        dp[i][j] = res
        return dp[i][j]

    def matrixMultiplication(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.helper(1, len(nums) - 1, nums, dp)


solution = Solution()
print(solution.matrixMultiplication([3, 7, 4, 5]) == 144)
print(solution.matrixMultiplication([1, 3, 1, 4, 1, 5]) == 13)
print(solution.matrixMultiplication([14, 30, 31, 74, 46, 33, 53, 19, 24, 73, 9, 15, 81, 47, 55, 20]) == 202653)
print(solution.matrixMultiplication(
    [35, 73, 90, 27, 71, 80, 21, 33, 33, 13, 48, 12, 68, 70, 80, 36, 66, 3, 70, 58]) == 140295)
