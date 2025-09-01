# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/

from typing import List
from heapq import heappush, heappop, heapify


class Solution:
    @staticmethod
    def connectSticks(sticks: List[int]) -> int:
        heapify(sticks)
        min_cost = 0
        while len(sticks) > 1:
            new_stick = heappop(sticks) + heappop(sticks)
            heappush(sticks, new_stick)
            min_cost += new_stick
        return min_cost


solution = Solution()
print(solution.connectSticks([2, 4, 3]) == 14)
print(solution.connectSticks([1, 8, 3, 5]) == 30)
print(solution.connectSticks([5]) == 0)
