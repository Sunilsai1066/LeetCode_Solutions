class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        Res = []
        for K,V in dict2.items():
            if(K in dict1):
                Res.extend([K]*min(V,dict1[K]))
        return Res
