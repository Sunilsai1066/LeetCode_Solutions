class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ResultArr = []
        def RecursiveCombinationSum(Ind,Arr,SubRes,ResultArr):
            ResultArr.append(SubRes.copy())
            for i in range(Ind,len(Arr)):
                if(i > Ind and Arr[i] == Arr[i-1]):continue
                SubRes.append(Arr[i])
                RecursiveCombinationSum(i+1,Arr,SubRes,ResultArr)
                SubRes.pop()
        RecursiveCombinationSum(0,nums,[],ResultArr)
        return ResultArr
