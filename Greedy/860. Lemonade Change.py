# https://leetcode.com/problems/lemonade-change/description/
from typing import List


class Solution:
    @staticmethod
    def lemonadeChange(bills: List[int]) -> bool:
        change_map = {
            5: 0,
            10: 0,
            20: 0
        }
        for num in bills:
            if num == 5:
                change_map[num] += 1
            elif num == 10:
                change_map[num] += 1
                change_map[5] -= 1
            else:
                change_map[num] += 1
                if change_map[10] > 0 and change_map[5] > 0:
                    change_map[10] -= 1
                    change_map[5] -= 1
                else:
                    change_map[5] -= 3
            if min(change_map.values()) < 0:
                return False
        return True


solution = Solution()
print(solution.lemonadeChange([5, 5, 5, 10, 20]) is True)
print(solution.lemonadeChange([5, 5, 10, 10, 20]) is False)
print(solution.lemonadeChange([10, 10]) is False)
print(solution.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]) is True)
print(solution.lemonadeChange([5, 5, 10, 20]) is True)
