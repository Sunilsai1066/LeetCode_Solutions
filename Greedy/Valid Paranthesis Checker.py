# https://takeuforward.org/plus/dsa/greedy-algorithms/hard/valid-paranthesis-checker

class Solution(object):
    @staticmethod
    def isValid(s):
        mini, maxi = 0, 0
        for ch in s:
            if ch == "(":
                mini += 1
                maxi += 1
            elif ch == ")":
                mini -= 1
                maxi -= 1
            else:
                maxi += 1
                mini -= 1
            if mini < 0:
                mini = 0
            if maxi < 0:
                return False
        return mini == 0 or maxi == 0


solution = Solution()
print(solution.isValid("(*))") is True)
print(solution.isValid("*(()") is False)
print(solution.isValid("(**()))") is True)
