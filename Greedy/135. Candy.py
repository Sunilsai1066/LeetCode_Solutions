# https://leetcode.com/problems/candy/description/

from typing import List


class Solution:
    @staticmethod
    def candy(ratings: List[int]) -> int:
        pre = [1] * len(ratings)
        post = [1] * len(ratings)
        min_candy = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                pre[i] = pre[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                post[i] = post[i + 1] + 1
        for i in range(len(ratings)):
            min_candy += max(pre[i], post[i])
        return min_candy


solution = Solution()
print(solution.candy([1, 0, 2]) == 5)
print(solution.candy([1, 2, 2]) == 4)
print(solution.candy([1, 0, 5]) == 5)
print(solution.candy([1, 2, 1, 4, 5]) == 9)
