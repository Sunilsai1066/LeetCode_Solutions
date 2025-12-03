# https://leetcode.com/problems/base-7/description/

class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        num = abs(num)
        while num:
            res = str(num % 7) + res
            num = num // 7
        return sign + res
