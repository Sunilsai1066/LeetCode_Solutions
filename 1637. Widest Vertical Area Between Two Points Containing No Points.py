class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted(points[i][0] for i in range(len(points)))
        maxi = 0
        for i in range(len(arr)-1, 0, -1):
            maxi = max(arr[i] - arr[i-1], maxi)
        return maxi
