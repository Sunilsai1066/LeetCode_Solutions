class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        FibSet = [1,1]
        A,B = 1,1
        while(FibSet[-1] < k):
            Val = FibSet[-1]+FibSet[-2]
            if(Val <= k):
                FibSet.append(Val)
            else:
                break
        Count = 0
        for i in range(len(FibSet)-1,-1,-1):
            if(FibSet[i] <= k):
                Count += 1
                k -= FibSet[i]
        return Count
