class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        Sum = 0
        while(piles):
            piles.pop()
            Sum += piles.pop()
            piles.pop(0)
        return Sum
