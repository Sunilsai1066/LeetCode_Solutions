from typing import List


class Solution:
    def helper(self, ind, prices, buy, dp, cap):
        if ind == len(prices):
            return 0
        if (ind, buy, cap) in dp:
            return dp[(ind, buy, cap)]
        if buy:
            ba = 0
            if ind > cap:
                ba = -prices[ind] + self.helper(ind + 1, prices, 0, dp, ind)
            bb = self.helper(ind + 1, prices, 1, dp, ind)
            dp[(ind, buy, cap)] = max(ba, bb)
        else:
            nba = prices[ind] + self.helper(ind + 1, prices, 1, dp, ind + 1)
            nbb = self.helper(ind + 1, prices, 0, dp, ind)
            dp[(ind, buy, cap)] = max(nba, nbb)
        return dp[(ind, buy, cap)]

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        return self.helper(0, prices, 1, dp, -1)
