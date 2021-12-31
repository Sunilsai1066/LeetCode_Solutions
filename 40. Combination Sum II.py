class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        FinRes = []
        
        def Helper(Ind,arr,target,FinRes,ds):
            if(target == 0):
                FinRes.append(ds.copy())
                return
            for i in range(Ind,len(candidates)):
                if(i > Ind and candidates[i] == candidates[i-1]):
                    continue
                if(candidates[i] > target):
                    break
                ds.append(candidates[i])
                Helper(i+1,candidates,target-candidates[i],FinRes,ds)
                ds.pop()
                
        Helper(0,candidates,target,FinRes,[])
        return FinRes
