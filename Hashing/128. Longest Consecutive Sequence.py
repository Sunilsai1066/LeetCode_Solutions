# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List


class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        nums.sort()
        counter = {}
        for num in nums:
            if num not in counter:
                if num - 1 in counter:
                    counter[num] = counter[num - 1] + 1
                else:
                    counter[num] = 1
        return max(counter.values())


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
print(solution.longestConsecutive([1, 0, 1, 2]) == 3)
