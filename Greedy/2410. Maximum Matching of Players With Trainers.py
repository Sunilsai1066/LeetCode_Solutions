# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
from typing import List


class Solution:
    @staticmethod
    def matchPlayersAndTrainers(players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ind1, ind2 = len(players) - 1, len(trainers) - 1
        count = 0
        while ind1 >= 0 and ind2 >= 0:
            if players[ind1] <= trainers[ind2]:
                count += 1
                ind1 -= 1
                ind2 -= 1
            else:
                ind1 -= 1
        return count


solution = Solution()
print(solution.matchPlayersAndTrainers([1, 2, 3, 7, 8, 9], [1, 2, 7, 9]) == 4)
print(solution.matchPlayersAndTrainers([1, 2], [1, 2, 3]) == 2)
print(solution.matchPlayersAndTrainers([1, 2, 3], [1, 1]) == 1)
print(solution.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]) == 2)
print(solution.matchPlayersAndTrainers([1, 1, 1], [10]) == 1)
