# https://leetcode.com/problems/assign-cookies/
from typing import List


class Solution:
    @staticmethod
    def findContentChildren(g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ind1, ind2 = len(g) - 1, len(s) - 1
        count = 0
        while ind1 >= 0 and ind2 >= 0:
            if g[ind1] <= s[ind2]:
                count += 1
                ind1 -= 1
                ind2 -= 1
            else:
                ind1 -= 1
        return count


solution = Solution()
print(solution.findContentChildren([1, 2, 3, 7, 8, 9], [1, 2, 7, 9]) == 4)
print(solution.findContentChildren([1, 2], [1, 2, 3]) == 2)
print(solution.findContentChildren([1, 2, 3], [1, 1]) == 1)
