class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        Dict1 = {V:K for K,V in enumerate(list1)}
        Min = float("inf")
        Res = []
        for i in range(len(list2)):
            if(list2[i] in Dict1):
                Val = i+Dict1[list2[i]]
                if(Val < Min):
                    Min = Val
                    Res = []
                    Res.append(list2[i])
                elif(Val == Min):
                    Res.append(list2[i])
        return Res
