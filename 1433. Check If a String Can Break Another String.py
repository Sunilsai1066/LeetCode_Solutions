class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        Score,Eq = 0,0
        for i in range(len(s1)):
            A,B = ord(s1[i]),ord(s2[i])
            if(A == B):
                Eq += 1
            elif(A > B):
                Score += 1
            elif(A < B):
                Score -= 1
        return abs(Score)+Eq == len(s1)
