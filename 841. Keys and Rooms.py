class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        Visit = set()
        def DFS(Node,Visit):
            Visit.add(Node)
            for i in rooms[Node]:
                if i not in Visit:
                    DFS(i,Visit)
        DFS(0,Visit)
        return len(Visit) == len(rooms)
