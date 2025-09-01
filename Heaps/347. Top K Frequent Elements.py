# https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List
from collections import Counter
from heapq import heapify, heappush, heappop


# Using Sorting
class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        count = [(v, k) for k, v in counter.items()]
        count.sort(reverse=True)
        return [count[i][1] for i in range(k)]


# Using Heap
class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], limit: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for k, v in counter.items():
            bucket[v].append(k)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                ind = 0
                while limit > 0 and ind < len(bucket[i]):
                    res.append(bucket[i][ind])
                    limit -= 1
                    ind += 1
                if limit == 0:
                    break
        return res


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2])
print(solution.topKFrequent([1], 1) == [1])
print(solution.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2])
