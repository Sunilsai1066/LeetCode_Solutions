class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        FinRes = []
        Map = [False for i in range(len(nums))]
        def ArrayPermutations(Arr,SubRes,FinRes,Map):
            if(len(SubRes) == len(Arr)):
                FinRes.append(SubRes.copy())
                return
            for i in range(len(Arr)):
                if(not Map[i]):
                    SubRes.append(Arr[i])
                    Map[i] = True
                    ArrayPermutations(Arr,SubRes,FinRes,Map)
                    SubRes.pop()
                    Map[i] = False
        ArrayPermutations(nums,[],FinRes,Map)
        return FinRes
