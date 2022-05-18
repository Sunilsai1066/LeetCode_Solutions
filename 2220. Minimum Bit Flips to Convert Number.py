class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        Count = 0
        for i in range(31, -1, -1):
            if(((start >> i)&1) != ((goal >> i)&1)):
                Count += 1
        return Count
