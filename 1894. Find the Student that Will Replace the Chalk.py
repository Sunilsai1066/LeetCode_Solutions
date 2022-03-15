class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        Total = sum(chalk)
        Rem = k%Total
        if(Rem == 0):
            return Rem
        for i in range(len(chalk)):
            if(Rem < chalk[i]):
                return i
            Rem -= chalk[i]
