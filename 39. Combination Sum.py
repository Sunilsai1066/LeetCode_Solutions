#Using Recursion
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.FinRes = []
        N = len(candidates)
        def Helper(Ind,candidates,SubRes,target,N):
            if(Ind == N or target <= 0):
                if(target == 0):
                    self.FinRes.append(SubRes.copy())
                    return
                return
            SubRes.append(candidates[Ind])
            Helper(Ind,candidates,SubRes,target-candidates[Ind],N)
            SubRes.pop()
            Helper(Ind+1,candidates,SubRes,target,N)
        Helper(0,candidates,[],target,N)
        return self.FinRes
