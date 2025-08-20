from typing import List


class Solution:
    def is_palindrome(self, palindromes, s):
        for i in range(len(s)):
            palindromes[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                palindromes[i][i + 1] = True
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and palindromes[i + 1][j - 1]:
                    palindromes[i][j] = True

    def helper(self, i, s, palindromes, dp):
        if i >= len(s):
            return 0
        if i in dp:
            return dp[i]
        cuts = float("inf")
        for k in range(i, len(s)):
            if palindromes[i][k]:
                subres = 1 + self.helper(k + 1, s, palindromes, dp)
                cuts = min(cuts, subres)
        dp[i] = cuts
        return dp[i]

    def minCut(self, s: str) -> int:
        dp = {}
        palindromes = [[False for _ in range(len(s))] for _ in range(len(s))]
        self.is_palindrome(palindromes, s)
        return self.helper(0, s, palindromes, dp) - 1


solution = Solution()
print(solution.minCut("aab") == 1)
print(solution.minCut("a") == 0)
print(solution.minCut("ab") == 1)
print(solution.minCut("bababcbadcede") == 4)
