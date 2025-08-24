# https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List


class Solution:
    @staticmethod
    def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count, prev = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1] and intervals[i][1] <= intervals[prev][1]:
                count += 1
                prev = i
            elif intervals[i][0] < intervals[prev][1] <= intervals[i][1]:
                count += 1
            else:
                prev = i
        return count


solution = Solution()
print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1)
print(solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2)
print(solution.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0)
print(solution.eraseOverlapIntervals([[1, 100], [2, 10], [16, 25], [30, 60], [70, 80], [87, 93]]) == 1)
print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [4, 5]]) == 0)
print(solution.eraseOverlapIntervals([[1, 10], [2, 3], [3, 4], [4, 5]]) == 1)
print(solution.eraseOverlapIntervals([[1, 5], [2, 6], [3, 7], [4, 8]]) == 3)
print(solution.eraseOverlapIntervals([[1, 2]]) == 0)
print(solution.eraseOverlapIntervals([[1, 2], [1, 3]]) == 1)
print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [1, 3], [3, 4]]) == 1)
print(solution.eraseOverlapIntervals([[1, 100], [101, 200], [201, 300]]) == 0)
print(solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2], [2, 3]]) == 2)
print(solution.eraseOverlapIntervals([[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 4)
print(solution.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2)
print(solution.eraseOverlapIntervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == 2)
