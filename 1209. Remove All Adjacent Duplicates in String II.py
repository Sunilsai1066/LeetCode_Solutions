class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        Stack = [(s[0],1)]
        for i in range(1,len(s)):
            Ch = s[i]
            if(Stack and Ch == Stack[-1][0]):
                Stack.append((Ch,Stack[-1][1]+1))
                if(Stack[-1][1] == k):
                    for i in range(k):
                        Stack.pop()
            else:
                Stack.append((Ch,1))
        Res = ""
        for Ch,Val in Stack:
            Res += Ch
        return Res
