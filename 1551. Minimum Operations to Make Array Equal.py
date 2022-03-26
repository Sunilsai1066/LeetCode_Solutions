O(1) Solution Exist

Time - O(n)
Space - O(n)

class Solution:
    def minOperations(self, n: int) -> int:
        Sum = 0
        Arr = []
        for i in range(n):
            Val = (2*i)+1
            Arr.append(Val)
            Sum += Val
        Avg = Sum//len(Arr)
        Res = 0
        for i in range(len(Arr)//2):
            Res += abs(Arr[i]-Avg)
        return Res


Time - O(n)
Space - O(n)

class Solution:
    def minOperations(self, n: int) -> int:
        Res = 0
        for i in range(n//2):
            Res += (n-((2*i)+1))
        return Res
