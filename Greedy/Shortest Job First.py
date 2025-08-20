# https://takeuforward.org/plus/dsa/greedy-algorithms/scheduling-and-interval-problems/shortest-job-first


class Solution:
    @staticmethod
    def solve(bt):
        bt.sort()
        wait = 0
        total_wait = 0
        for i in range(1, len(bt)):
            wait += bt[i - 1]
            total_wait += wait
        return total_wait // len(bt)


solution = Solution()
print(solution.solve([4, 1, 3, 7, 2]) == 4)
print(solution.solve([1, 2, 3, 4]) == 2)
print(solution.solve([9, 3, 1, 8, 2]) == 4)
