# https://takeuforward.org/plus/dsa/greedy-algorithms/scheduling-and-interval-problems/n-meetings-in-one-room

class Solution:
    @staticmethod
    def maxMeetings(start, end):
        meetings = [[start[i], end[i]] for i in range(len(start))]
        meetings.sort(key=lambda x: x[1])
        prev, count = -1, 0
        for start, end in meetings:
            if start > prev:
                prev = end
                count += 1
        return count


solution = Solution()
print(solution.maxMeetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]) == 4)
print(solution.maxMeetings([10, 12, 20], [20, 25, 30]) == 1)
print(solution.maxMeetings([1, 4, 6, 9], [2, 5, 7, 12]) == 4)
