class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsSort = sorted(nums)
        Start, End = 0, len(nums)-1
        while(Start < End):
            if(nums[Start] == numsSort[Start] and nums[End] == numsSort[End]):
                Start += 1
                End -= 1
            elif(nums[Start] == numsSort[Start]):
                Start += 1
            elif(nums[End] == numsSort[End]):
                End -= 1
            else:
                return End-Start+1
        return 0
