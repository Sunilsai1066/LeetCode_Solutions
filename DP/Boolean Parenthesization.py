# https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1

# Memoization With Dictionary
class Solution:
    def helper(self, i, j, s, is_true, dp):
        if i > j:
            return 0
        if i == j:
            if is_true:
                if s[i] == "T":
                    return 1
                return 0
            if s[i] == "F":
                return 1
            return 0
        ways = 0
        if (i, j, is_true) in dp:
            return dp[(i, j, is_true)]
        for k in range(i + 1, j, 2):
            rt = self.helper(i, k - 1, s, 1, dp)
            rf = self.helper(i, k - 1, s, 0, dp)
            lt = self.helper(k + 1, j, s, 1, dp)
            lf = self.helper(k + 1, j, s, 0, dp)
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
        dp[(i, j, is_true)] = ways
        return dp[(i, j, is_true)]

    def countWays(self, s):
        dp = {}
        return self.helper(0, len(s)-1, s, 1, dp)


# Memoization Using 3D Array
class Solution:
    def helper(self, i, j, s, is_true, dp):
        if i > j:
            return 0
        if i == j:
            if is_true:
                if s[i] == "T":
                    return 1
                return 0
            if s[i] == "F":
                return 1
            return 0
        ways = 0
        if dp[i][j][is_true] != -1:
            return dp[i][j][is_true]
        for k in range(i + 1, j, 2):
            rt = self.helper(i, k - 1, s, 1, dp)
            rf = self.helper(i, k - 1, s, 0, dp)
            lt = self.helper(k + 1, j, s, 1, dp)
            lf = self.helper(k + 1, j, s, 0, dp)
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
        return dp[i][j][is_true]

    def countWays(self, s):
        n = len(s)
        dp = [[[-1 for _ in range(2)] for _ in range(n)]for _ in range(n)]
        return self.helper(0, n-1, s, 1, dp)

# Tabulation

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
