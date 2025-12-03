# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b:
            tot = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = tot, carry
        return a if a <= MAX_INT else a - (2**32)
