# Memoization
class Solution:
    def helper(self, i, j, nums):
        if i == j:
            return 0
        res = float("inf")
        for k in range(i, j):
            subres = (nums[k] * nums[i - 1] * nums[j]) + self.helper(i, k, nums) + self.helper(k + 1, j, nums)
            res = min(res, subres)
        return res

    def matrixMultiplication(self, nums):
        return self.helper(1, len(nums) - 1, nums)


solution = Solution()
print(solution.matrixMultiplication([1, 2, 3, 4]) == 18)


# Tabulation

from typing import List


class Solution:
    @staticmethod
    def matrixMultiplication(nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n):
                res = float("inf")
                for k in range(i, j):
                    if i == j:
                        continue
                    subres = (nums[k] * nums[i - 1] * nums[j]) + dp[i][k] + dp[k + 1][j]
                    res = min(res, subres)
                dp[i][j] = res
        return dp[1][n - 1]


solution = Solution()
print(solution.matrixMultiplication([1, 2, 3]) == 6)
print(solution.matrixMultiplication([3, 7, 4, 5]) == 144)
print(solution.matrixMultiplication([1, 3, 1, 4, 1, 5]) == 13)
print(solution.matrixMultiplication([14, 30, 31, 74, 46, 33, 53, 19, 24, 73, 9, 15, 81, 47, 55, 20]) == 202653)
print(solution.matrixMultiplication(
    [35, 73, 90, 27, 71, 80, 21, 33, 33, 13, 48, 12, 68, 70, 80, 36, 66, 3, 70, 58]) == 140295)