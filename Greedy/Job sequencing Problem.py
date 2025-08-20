# https://takeuforward.org/plus/dsa/greedy-algorithms/scheduling-and-interval-problems/job-sequencing-problem

class Solution:
    @staticmethod
    def JobScheduling(Jobs):
        count, profit = 0, 0
        max_day = 0
        Jobs.sort(key=lambda x: x[2], reverse=True)
        for job in Jobs:
            max_day = max(max_day, job[1])
        track = [-1] * (max_day + 1)
        for job_id, deadline, money in Jobs:
            if track[deadline] == -1:
                track[deadline] = job_id
                count += 1
                profit += money
            else:
                ind = deadline - 1
                while ind > 0:
                    if track[ind] == -1:
                        track[ind] = job_id
                        count += 1
                        profit += money
                        break
                    else:
                        ind -= 1
        return count, profit


solution = Solution()
print(solution.JobScheduling([[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]) == (2, 60))
print(solution.JobScheduling([[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]) == (2, 127))
print(solution.JobScheduling([[1, 1, 100], [2, 2, 200], [3, 3, 300], [4, 4, 400]]) == (4, 1000))
print(solution.JobScheduling([[10, 10, 20], [20, 10, 300], [3, 5, 1], [2, 9, 900]]) == (4, 1221))
