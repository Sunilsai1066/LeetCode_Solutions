class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        Digits = [int(i) for i in s.split(" ") if(i.isdigit())]
        for i in range(1,len(Digits)):
            if(Digits[i-1] >= Digits[i]):
                return False
        return True
