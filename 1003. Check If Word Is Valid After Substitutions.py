class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%3 != 0):
            return False
        Stack = []
        for ch in s:
            if(ch == "b"):
                if(Stack and Stack[-1] == "a"):
                    Stack.pop()
                    Stack.append(ch)
                else:
                    Stack.append(ch)
            elif(ch == "c"):
                if(Stack and Stack[-1] == "b"):
                    Stack.pop()
                else:
                    Stack.append(ch)
            elif(ch == "a"):
                if(Stack and Stack[-1] == "c"):
                    Stack.pop()
                    Stack.append(ch)
                else:
                    Stack.append(ch)
        return len(Stack) == 0
