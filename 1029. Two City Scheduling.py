class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        firstSum = 0
        for I,J in costs:
            firstSum += I
        diffLis = [J-I for I,J in costs]
        diffLis.sort()
        return firstSum + sum(diffLis[:len(costs)//2])
