class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        Count = 0
        while(left != right):
            left >>= 1
            right >>= 1
            Count += 1
        return left << Count
