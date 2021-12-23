class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        Len = len(nums)
        Start,End = 0,1
        while(End < Len):
            if(nums[Start] == nums[End] == 0):
                End += 1
            elif(nums[Start]==0 and nums[End]!=0):
                nums[Start],nums[End] = nums[End],nums[Start]
                Start += 1
                End += 1
            else:
                Start += 1
                End += 1
