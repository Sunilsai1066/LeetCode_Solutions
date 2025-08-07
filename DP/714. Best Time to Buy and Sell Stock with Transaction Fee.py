from typing import List


class Solution:
    @staticmethod
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    ba = -prices[ind] + dp[ind + 1][0]
                    bb = dp[ind + 1][buy]
                    dp[ind][buy] = max(ba, bb)
                else:
                    nba = prices[ind] - fee + dp[ind + 1][1]
                    nbb = dp[ind + 1][buy]
                    dp[ind][buy] = max(nba, nbb)
        return dp[0][1]
