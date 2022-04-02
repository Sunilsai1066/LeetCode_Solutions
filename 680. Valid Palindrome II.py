class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(Sub):
            Start,End = 0,len(Sub)-1
            while(Start <= End):
                if(Sub[Start] != Sub[End]):
                    return False
                Start += 1
                End -= 1
            return True
        
        Start,End = 0,len(s)-1
        while(Start <= End):
            if(s[Start] != s[End]):
                if(helper(s[Start:End])):
                    return True
                return helper(s[Start+1:End+1])
            Start += 1
            End -= 1
        return True
