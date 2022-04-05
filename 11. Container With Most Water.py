class Solution:
    def maxArea(self, height: List[int]) -> int:
        Len = len(height)
        Start,End = 0,Len-1
        Lines = Len-1
        MaxYet = 0
        while(Start < End):
            MaxSoFar = min(height[Start],height[End])*Lines
            MaxYet = max(MaxYet,MaxSoFar)
            if(height[Start] < height[End]):
                Start += 1
            else:
                End -= 1
            Lines -= 1
        return MaxYet
