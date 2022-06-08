class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        finRes = []
        def helper(Out, Open, Close):
            if(Open == Close == 0):
                finRes.append(Out)
                return
            elif(Open == 0):
                rem = ")"*Close
                finRes.append(Out+rem)
                return
            if(Open == Close):
                helper(Out+"(", Open-1, Close)
            else:
                helper(Out+"(", Open-1, Close)
                helper(Out+")", Open, Close-1)

        helper("", n, n)
        return finRes
