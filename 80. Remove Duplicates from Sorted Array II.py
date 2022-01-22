class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Len = len(nums)
        if(Len <= 2):return Len
        Prev = nums[0]
        Ind = 1
        Count = 1
        while(Ind < Len):
            if(Prev == nums[Ind]):
                Count += 1
                if(Count > 2):
                    nums.pop(Ind)
                    Len -= 1
                else:
                    Ind += 1
            else:
                Prev = nums[Ind]
                Count = 1
                Ind += 1
        return Ind
