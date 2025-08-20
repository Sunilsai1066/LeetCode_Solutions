# https://leetcode.com/problems/meeting-rooms/description/

from typing import List


class Solution:
    @staticmethod
    def canAttendMeetings(intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[1])
        prev, count = -1, 0
        for start, end in intervals:
            if start >= prev:
                prev = end
                count += 1
            else:
                return False
        return True


solution = Solution()
print(solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False)
print(solution.canAttendMeetings([[7, 10], [2, 4]]) is True)
