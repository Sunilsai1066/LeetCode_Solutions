# https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1

class Solution:
    @staticmethod
    def countWays(s):
        n = len(s)
        dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(0, n):
                for is_true in [1, 0]:
                    if i == j:
                        if is_true:
                            if s[i] == "T":
                                dp[i][j][is_true] = 1
                        else:
                            if s[i] == "F":
                                dp[i][j][is_true] = 1
                    else:
                        ways = 0
                        for k in range(i + 1, j, 2):
                            rt = dp[i][k - 1][1]
                            rf = dp[i][k - 1][0]
                            lt = dp[k + 1][j][1]
                            lf = dp[k + 1][j][0]
                            if s[k] == "&":
                                if is_true:
                                    ways += (rt * lt)
                                else:
                                    ways += ((rt * lf) + (rf * lt) + (rf * lf))
                            elif s[k] == "|":
                                if is_true:
                                    ways += ((rt * lt) + (rt * lf) + (lt * rf))
                                else:
                                    ways += (rf * lf)
                            else:
                                if is_true:
                                    ways += ((rt * lf) + (rf * lt))
                                else:
                                    ways += ((rt * lt) + (rf * lf))
                        dp[i][j][is_true] = ways
        return dp[0][n - 1][1]


solution = Solution()
print(solution.countWays(s="T|T&F^T") == 4)
print(solution.countWays(s="T^T|F^T") == 4)
print(solution.countWays(s="T^F|F") == 2)
print(solution.countWays(s="F&T|T|T&F") == 2)
print(solution.countWays(s="F&T|T|T&F^T") == 23)
print(solution.countWays("T|F") == 1)
print(solution.countWays("T|F^T") == 1)
print(solution.countWays("T&T|F^T") == 2)
print(solution.countWays("T") == 1)
