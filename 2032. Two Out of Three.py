class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ResHash = {}
        for i in nums1:
            if i not in ResHash:
                ResHash[i] = [1,0,0,1]
        for i in nums2:
            if i not in ResHash:
                ResHash[i] = [0,1,0,1]
            elif(ResHash[i][1] == 0):
                ResHash[i][1] = 1
                ResHash[i][3] += 1
        for i in nums3:
            if i not in ResHash:
                ResHash[i] = [0,0,1,1]
            elif(ResHash[i][2] == 0):
                ResHash[i][2] = 1
                ResHash[i][3] += 1
        Res = []
        for K,V in ResHash.items():
            if(V[3] >= 2):
                Res.append(K)
        return Res
