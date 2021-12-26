class Solution:
    def search(self, nums: List[int], target: int) -> int:
        Start,End = 0,len(nums)-1
        Ind = -1
        while(Start <= End):
            Mid = (Start+End)//2
            if(nums[Mid] == target):
                return Mid
            elif(nums[Mid] < target):
                Start = Mid+1
            else:
                End = Mid-1
        return -1
