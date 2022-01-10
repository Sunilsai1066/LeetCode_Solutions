class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.Dict = {}
        for i in range(len(self.nums)):
            if self.nums[i] not in self.Dict:
                self.Dict[self.nums[i]] = [i]
            else:
                self.Dict[self.nums[i]].append(i)
    def pick(self, target: int) -> int:
        return random.choice(self.Dict[target])
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
