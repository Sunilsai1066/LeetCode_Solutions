class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        DishDict,ItemSet = {},set()
        for CName,Table,Item in orders:
            if(int(Table) not in DishDict):
                DishDict[int(Table)] = {Item : 1}
                ItemSet.add(Item)
            elif(int(Table) in DishDict and Item not in DishDict[int(Table)]):
                DishDict[int(Table)][Item] = 1
                ItemSet.add(Item)
            else:
                DishDict[int(Table)][Item] += 1
        ItemList = list(ItemSet)
        ItemList.sort()
        Result = []
        for K,V in sorted(DishDict.items()):
            SubLis = []
            SubLis.append(str(K))
            for Item in ItemList:
                if Item in V:
                    SubLis.append(str(V[Item]))
                else:
                    SubLis.append("0")
            Result.append(SubLis)
            SubLis = []
        ItemList.insert(0,"Table")
        Result.insert(0,ItemList)
        return Result
