from typing import List


class Solution:
    @staticmethod
    def isValid(nums1, nums2) -> bool:
        if (nums1 % nums2 == 0) or (nums2 % nums1 == 0):
            return True
        return False

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)
        res = [i for i in range(len(nums))]
        nums.sort()
        for i in range(len(nums)):
            maxi = 1
            for j in range(i):
                if nums[j] < nums[i] and self.isValid(nums[i], nums[j]):
                    if dp[j] + 1 > maxi:
                        maxi = dp[j] + 1
                        res[i] = j
            dp[i] = maxi
        maxi, max_ind, ind = 0, 0, 0
        for i in range(len(nums)):
            if dp[i] > maxi:
                max_ind = i
                maxi = dp[i]
                ind = res[i]
        subres = [nums[max_ind]]
        while max_ind != ind:
            subres.append(nums[ind])
            max_ind, ind = ind, res[ind]
        subres.reverse()
        return subres


solution = Solution()
print([1, 2] == solution.largestDivisibleSubset([1, 2, 3]))
print([1, 2, 4, 8] == solution.largestDivisibleSubset([1, 2, 4, 8]))
