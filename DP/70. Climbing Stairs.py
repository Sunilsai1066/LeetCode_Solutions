# https://leetcode.com/problems/climbing-stairs/

from typing import List


# Memoization
class Solution:
    def helper(self, n, dp):
        if n <= 2:
            dp[n] = n
            return n
        if n in dp:
            return dp[n]
        first = self.helper(n - 1, dp)
        second = self.helper(n - 2, dp)
        dp[n] = first + second
        return dp[n]

    def climbStairs(self, n: int) -> int:
        return self.helper(n, {})


# Tabulation With Memory Optimization
class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            curr, prev = prev + curr, curr
        return curr


solution = Solution()
print(solution.climbStairs(2) == 2)
print(solution.climbStairs(3) == 3)
print(solution.climbStairs(5) == 8)
print(solution.climbStairs(10) == 89)
print(solution.climbStairs(20) == 10946)
print(solution.climbStairs(35) == 14930352)
