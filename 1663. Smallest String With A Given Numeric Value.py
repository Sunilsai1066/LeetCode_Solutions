class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        Res = [1]*n
        k -= n
        Ind = n-1
        while(k > 0):
            Val = min(25,k)
            Res[Ind] += Val
            k -= Val
            Ind -= 1
        Str = ""
        for i in Res:
            Str += chr(96+i)
        return Str
