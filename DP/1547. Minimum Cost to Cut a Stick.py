from typing import List


class Solution:
    def helper(self, i, j, cuts, dp):
        if i > j:
            return 0
        if (i, j) in dp:
            return dp[(i, j)]
        res = float('inf')
        for k in range(i, j + 1):
            subres = (cuts[j + 1] - cuts[i - 1]) + self.helper(i, k - 1, cuts, dp) + self.helper(k + 1, j, cuts, dp)
            res = min(res, subres)
        dp[(i, j)] = res
        return dp[(i, j)]

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)
        dp = {}
        return self.helper(1, len(cuts) - 2, cuts, dp)


solution = Solution()
print(solution.minCost(n=7, cuts=[1, 3, 4]) == 14)
print(solution.minCost(n=7, cuts=[1, 3, 4, 5]) == 16)
print(solution.minCost(9, [5, 6, 1, 4, 2]) == 22)
