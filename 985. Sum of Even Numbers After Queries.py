class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        TotSum = sum([i for i in nums if(i%2==0)])
        Res = []
        print(TotSum)
        for Val,Ind in queries:
            if(nums[Ind] % 2 == 0):
                Prev = nums[Ind]
                nums[Ind] += Val
                if(nums[Ind] % 2 == 0):
                    TotSum += Val
                else:
                    TotSum -= Prev
                Res.append(TotSum)
            else:
                nums[Ind] += Val
                if(nums[Ind]%2==0):
                    TotSum += nums[Ind]
                Res.append(TotSum)
        return Res
