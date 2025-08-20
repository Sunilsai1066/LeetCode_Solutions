from typing import List


class Solution:
    def helper(self, i, arr, limit, dp):
        if i >= len(arr):
            return 0
        res = float("-inf")
        if (i, limit) in dp:
            return dp[(i, limit)]
        maxi = 0
        for k in range(i, min(len(arr), i + limit)):
            count = (k - i) + 1
            maxi = max(maxi, arr[k])
            subres = (maxi * count) + self.helper(k + 1, arr, limit, dp)
            res = max(res, subres)
        dp[(i, limit)] = res
        return dp[(i, limit)]

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {}
        return self.helper(0, arr, k, dp)


solution = Solution()
print(solution.maxSumAfterPartitioning(arr=[1, 15], k=1) == 16)
print(solution.maxSumAfterPartitioning(arr=[1, 15], k=2) == 30)
print(solution.maxSumAfterPartitioning(arr=[1, 15, 7], k=2) == 37)
print(solution.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2], k=3) == 63)
print(solution.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3) == 84)
print(solution.maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4) == 83)
print(solution.maxSumAfterPartitioning(arr=[1], k=1) == 1)
