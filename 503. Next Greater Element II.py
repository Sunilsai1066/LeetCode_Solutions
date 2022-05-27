class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        Len = len(nums)
        res = [-1]*Len
        stack = []
        for i in range(2*Len-1, -1, -1):
            while(stack and stack[-1] <= nums[i%Len]):
                stack.pop()
            if(stack):
                res[i%Len] = stack[-1]
            else:
                res[i%Len] = -1
            stack.append(nums[i%Len])
        return res
