# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List


class Solution:
    @staticmethod
    def minMeetingRooms(intervals: List[List[int]]) -> int:
        start, end = [], []
        for st, en in intervals:
            start.append(st)
            end.append(en)
        start.sort()
        end.sort()
        count, res = 0, 0
        ind1, ind2 = 0, 0
        while ind1 < len(intervals):
            if start[ind1] < end[ind2]:
                count += 1
                ind1 += 1
                res = max(count, res)
            else:
                count -= 1
                ind2 += 1
        return res


solution = Solution()
print(solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2)
print(solution.minMeetingRooms([[7, 10], [2, 4]]) == 1)
