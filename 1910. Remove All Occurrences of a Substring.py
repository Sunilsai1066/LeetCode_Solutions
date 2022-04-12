class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        SubLen = len(part)
        Stack = []
        for i in s:
            Stack.append(i)
            if(len(Stack) >= SubLen and ''.join(Stack[len(Stack)-SubLen:])==part):
                for _ in range(SubLen):
                    Stack.pop()
        return "".join(Stack)
