class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for r in matrix:
            if(len(set(r)) != n):
                return False
        for c in list(zip(*matrix)):
            if(len(set(c)) != n):
                return False
        return True
