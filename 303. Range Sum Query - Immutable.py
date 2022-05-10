class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.PrefSum = []
        Start = 0
        for i in range(len(self.nums)):
            Start += self.nums[i]
            self.PrefSum.append(Start)

    def sumRange(self, left: int, right: int) -> int:
        if(left == 0):
            return self.PrefSum[right]
        else:
            return self.PrefSum[right]-self.PrefSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
