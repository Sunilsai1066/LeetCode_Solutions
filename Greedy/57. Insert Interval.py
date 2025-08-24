# https://leetcode.com/problems/insert-interval/description/

from typing import List


class Solution:
    @staticmethod
    def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
print(solution.insert([[1, 3], [6, 9], [10, 20], [24, 56]], [2, 100]) == [[1, 100]])
print(solution.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]])
print(solution.insert([[1, 5]], [5, 7]) == [[1, 7]])
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10]], [1, 8]) == [[1, 10]])
