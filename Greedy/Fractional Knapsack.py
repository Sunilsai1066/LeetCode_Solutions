# https://leetcode.com/discuss/post/1066692/fractional-knapsack-by-avneetsng-hp1c/


class Solution:
    @staticmethod
    def fractional_knapsack(knapsack, W):
        knapsack.sort(key=lambda x: (x[0] / x[1]), reverse=True)
        res = 0
        ind = 0
        while ind < len(knapsack) and W > 0:
            if knapsack[ind][1] <= W:
                res += knapsack[ind][0]
                W -= knapsack[ind][1]
            else:
                wt = (knapsack[ind][0] / knapsack[ind][1]) * W
                res += wt
                W = 0
            ind += 1
        return res


solution = Solution()
print(solution.fractional_knapsack([(100, 20), (60, 10), (100, 50), (200, 50)], 90) == 380)
