class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numSet = {int(i,2) for i in nums}
        Len = len(nums[0])
        for i in range(0,2**Len):
            if i not in numSet:
                res = bin(i)[2:]
                if(len(res) == Len):
                    return res
                subRes = '0'*(Len-len(res))
                return subRes+res
