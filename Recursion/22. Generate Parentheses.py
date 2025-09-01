# https://leetcode.com/problems/generate-parentheses/description/

from typing import List


class Solution:
    def helper(self, first, second, par, n, res):
        if first > n or second > n:
            return
        if first == second == n:
            res.append(par)
            return
        if second > first:
            return
        if par is None:
            par += "("
            self.helper(first + 1, second, par, n, res)
        else:
            self.helper(first + 1, second, par + "(", n, res)
            self.helper(first, second + 1, par + ")", n, res)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(0, 0, "", n, res)
        return res


solution = Solution()
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(4))
print(solution.generateParenthesis(5))