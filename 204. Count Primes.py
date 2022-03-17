class Solution:
    def countPrimes(self, n: int) -> int:
        if(n <= 1):
            return 0
        Res = [True]*n
        Res[0],Res[1] = False,False
        for i in range(2,int(n**0.5)+1):
            if(Res[i]):
                for j in range(i*i,n,i):
                    Res[j] = False
        return sum(Res)
