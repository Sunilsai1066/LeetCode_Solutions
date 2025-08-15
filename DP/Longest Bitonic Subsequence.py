# https://takeuforward.org/plus/dsa/dynamic-programming/lis-dp/longest-bitonic-subsequence

class Solution:
    @staticmethod
    def LongestBitonicSequence(arr):
        n = len(arr)
        dp1, dp2 = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j] and dp1[j] + 1 > dp1[i]:
                    dp1[i] = dp1[j] + 1
        arr.reverse()
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j] and dp2[j] + 1 > dp2[i]:
                    dp2[i] = dp2[j] + 1
        dp2.reverse()
        maxi = 1
        for i in range(n):
            maxi = max(maxi, dp1[i] + dp2[i] - 1)
        return maxi


solution = Solution()
print(6 == solution.LongestBitonicSequence([5, 1, 4, 2, 3, 6, 8, 7]))
print(8 == solution.LongestBitonicSequence([10, 20, 30, 40, 50, 40, 30, 20]))
print(6 == solution.LongestBitonicSequence([12, 11, 10, 15, 18, 17, 16, 14]))
