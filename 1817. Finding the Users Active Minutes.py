class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UniqueCount = {}
        for Id,Time in logs:
            if Id not in UniqueCount:
                Set = set()
                Set.add(Time)
                UniqueCount[Id] = [Set,1]
            elif(Time not in UniqueCount[Id][0]):
                UniqueCount[Id][0].add(Time)
                UniqueCount[Id][1] += 1
        Res = [0]*k
        for K,V in UniqueCount.items():
            Res[V[1]-1] += 1
        return Res
