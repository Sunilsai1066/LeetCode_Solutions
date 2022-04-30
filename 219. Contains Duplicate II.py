class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Map = {}
        for Ind,num in enumerate(nums):
            if(num not in Map):
                Map[num] = [Ind]
            else:
                Map[num].append(Ind)
                if(abs(Map[num][-1] - Map[num][-2]) <= k):
                    return True
