class Solution:
    def partition(self, s: str) -> List[List[str]]:
        Res = []
        def helper(s,Ind,subRes,N):
            if(Ind == N):
                Res.append(subRes[:])
                return
            for i in range(Ind,N):
                Sub = s[Ind:(i+1)]
                if(Sub == Sub[::-1]):
                    subRes.append(Sub)
                    helper(s,i+1,subRes,N)
                    subRes.pop()
        helper(s,0,[],len(s))
        return Res
