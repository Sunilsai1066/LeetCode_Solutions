# https://takeuforward.org/plus/dsa/greedy-algorithms/scheduling-and-interval-problems/minimum-number-of-platforms-required-for-a-railway

class Solution:
    @staticmethod
    def findPlatform(Arrival, Departure):
        Arrival = [int(num) for num in Arrival]
        Departure = [int(num) for num in Departure]
        Arrival.sort()
        Departure.sort()
        ind1, ind2 = 0, 0
        count, max_count = 0, 0
        while ind1 < len(Arrival):
            if Arrival[ind1] <= Departure[ind2]:
                count += 1
                ind1 += 1
            else:
                count -= 1
                ind2 += 1
            max_count = max(max_count, count)
        return max_count


solution = Solution()
print(solution.findPlatform(["0900", "0940", "0950", "1100", "1500", "1800"],
                            ["0910", "1200", "1120", "1130", "1900", "2000"]) == 3)
print(solution.findPlatform(["0900", "1100", "1235"], ["1000", "1200", "1240"]) == 1)
print(solution.findPlatform(["0900", "1100", "1235"], ["1300", "1200", "1240"]) == 2)
print(solution.findPlatform(["0930", "0950", "1000", "940", "1200", "1500"],
                            ["0950", "1030", "1230", "1320", "1520", "1800"]) == 3)
print(solution.findPlatform(["0900"], ["1230"]) == 1)
print(solution.findPlatform(["0900", "1000"], ["1000", "1100"]) == 2)
