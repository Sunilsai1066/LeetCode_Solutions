from typing import List


class Solution:
    @staticmethod
    def findNumberOfLIS(nums: List[int]) -> int:
        n = len(nums)
        dp, count = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] = count[i] + count[j]
        maxi = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == maxi:
                res += count[i]
        return res


solution = Solution()
print(2 == solution.findNumberOfLIS([1, 3, 2, 6]))
print(2 == solution.findNumberOfLIS([1, 3, 5, 4, 7]))
print(5 == solution.findNumberOfLIS([2, 2, 2, 2, 2]))
print(4 == solution.findNumberOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(3 == solution.findNumberOfLIS([3, 5, 8, 4, 7, 9, 10]))
print(2 == solution.findNumberOfLIS([3, 5, 4, 8]))
