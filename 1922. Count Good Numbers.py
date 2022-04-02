class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Even,Odd = (n//2+n%2),n//2
        return (pow(5,Even,1000000007)*pow(4,Odd,1000000007))%1000000007
