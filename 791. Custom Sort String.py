class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sCount = Counter(s)
        sSet = set()
        Res = ""
        for ch in order:
            if(ch in sCount):
                subRes = ch*sCount[ch]
                Res += subRes
                sSet.add(ch)
        for K,V in sCount.items():
            if(K not in sSet):
                subRes = K*V
                Res += subRes
        return Res
