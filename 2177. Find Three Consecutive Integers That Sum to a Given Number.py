class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if(num % 3 != 0):
            return []
        Res = num//3
        return [Res-1,Res,Res+1]
