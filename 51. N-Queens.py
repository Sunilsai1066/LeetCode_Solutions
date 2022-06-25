class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        Empty = [["." for j in range(n)]for i in range(n)]
        Map = {"col" : set(), "row" : set()}
        DownDiag = set()
        UpDiag = set()
        def helper(ind, fillArr):
            if(ind == n):
                subRes = ["".join(lis) for lis in fillArr]
                res.append(subRes[:])
                return
            for r in range(n):
                upVal = (n-1)+(ind-r)
                if(r not in Map["row"] and ind not in Map["col"] and r+ind not in DownDiag and upVal not in UpDiag):
                    fillArr[r][ind] = 'Q'
                    Map["row"].add(r)
                    Map["col"].add(ind)
                    DownDiag.add(r+ind)
                    UpDiag.add(upVal)
                    helper(ind+1, fillArr)
                    fillArr[r][ind] = '.'
                    Map["row"].remove(r)
                    Map["col"].remove(ind)
                    DownDiag.remove(r+ind)
                    UpDiag.remove(upVal)

        helper(0, Empty)
        return res
