class Solution:
    def longestIncreasingSubsequence(self, arr):
        n = len(arr)
        dp = [1] * n
        res = [i for i in range(n)]
        for i in range(n):
            maxi = 1
            for j in range(i):
                if arr[j] < arr[i]:
                    if dp[j] + 1 > maxi:
                        res[i] = j
                        maxi = dp[j] + 1
            dp[i] = maxi
        maxi, max_ind, ind = 0, 0, 0
        for i in range(n):
            if dp[i] > maxi:
                max_ind = i
                maxi = dp[i]
                ind = res[i]
        subres = [arr[max_ind]]
        while max_ind != ind:
            subres.append(arr[ind])
            max_ind, ind = ind, res[ind]
        subres.reverse()
        return subres


solution = Solution()
print([10, 22, 33, 50, 60, 80] == solution.longestIncreasingSubsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print([1, 3, 4, 6] == solution.longestIncreasingSubsequence([1, 3, 2, 4, 6, 5]))
print([1, 2, 3, 4, 7] == solution.longestIncreasingSubsequence([5, 6, 1, 2, 3, 4, 7]))
