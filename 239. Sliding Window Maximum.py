class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        numsDeque = deque()
        for i in range(len(nums)):
            while(numsDeque and numsDeque[0]<=(i-k)):
                numsDeque.popleft()
            while(numsDeque and nums[numsDeque[-1]] <= nums[i]):
                numsDeque.pop()
            numsDeque.append(i)
            if(i >= k-1):
                res.append(nums[numsDeque[0]])
        return res
