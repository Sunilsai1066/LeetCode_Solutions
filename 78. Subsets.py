#Recursion Solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        FinRes = []
        Start,End = 0,len(nums)-1
        def subSets(Lis,Res,Start,End,FinRes):
            if(Start > End):
                FinRes.append(Res[:])
                return
            Res.append(Lis[Start])
            subSets(Lis,Res,Start+1,End,FinRes)
            Res.pop()
            subSets(Lis,Res,Start+1,End,FinRes)
        subSets(nums,[],Start,End,FinRes)
        return FinRes

#Power Set Method
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Res = []
        n = len(nums)
        for i in range(2**n):
            SubLis = []
            for j in range(n):
                if(i & (1<<j)):
                    SubLis.append(nums[j])
            Res.append(SubLis)
        return Res
