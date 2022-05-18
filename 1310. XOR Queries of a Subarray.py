class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        PrefXOR = [arr[0]]
        for i in range(1, len(arr)):
            PrefXOR.append(PrefXOR[-1]^arr[i])
        print(PrefXOR)
        Res = []
        for St, En in queries:
            if(St == 0):
                Res.append(PrefXOR[En])
            else:
                Res.append(PrefXOR[En]^PrefXOR[St-1])
        return Res
