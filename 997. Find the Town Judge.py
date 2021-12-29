class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Judge = [0]*(n+1)
        for I,O in trust:
            Judge[I] -= 1
            Judge[O] += 1
        for J in range(1,n+1):
            if(Judge[J] == n-1):
                return J
        return -1
