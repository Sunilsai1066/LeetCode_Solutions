class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        Grps = {}
        for i in range(len(groupSizes)):
            if(groupSizes[i] not in Grps):
                Grps[groupSizes[i]] = [i]
            else:
                Grps[groupSizes[i]].append(i)
        Res = []
        SubLis = []
        for i in Grps.keys():
            for j in Grps[i]:
                SubLis.append(j)
                if(len(SubLis) == i):
                    Res.append(SubLis)
                    SubLis = []
        return Res
