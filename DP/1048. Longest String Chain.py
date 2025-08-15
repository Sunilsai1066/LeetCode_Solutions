from typing import List


class Solution:
    @staticmethod
    def is_increasing(word1, word2) -> bool:
        if len(word1) + 1 != len(word2):
            return False
        ind1, ind2 = 0, 0
        while ind2 < len(word2):
            if ind1 < len(word1) and word1[ind1] == word2[ind2]:
                ind1 += 1
                ind2 += 1
            else:
                ind2 += 1
        if ind1 == len(word1) and ind2 == len(word2):
            return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = [1] * len(words)
        for i in range(len(words)):
            maxi = 1
            for j in range(i):
                if self.is_increasing(words[j], words[i]) and dp[i] < dp[j] + 1:
                    maxi = max(maxi, dp[j] + 1)
            dp[i] = maxi
        return max(dp)


solution = Solution()
print(4 == solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(5 == solution.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(1 == solution.longestStrChain(["abcd", "dbqca"]))
print(5 == solution.longestStrChain(["a", "ab", "abc", "abcd", "abcde"]))
print(4 == solution.longestStrChain(["dog", "dogs", "dots", "dot", "d", "do"]))
print(4 == solution.longestStrChain(["a", "aa", "aaa", "aaaa", "b", "bb", "bbb"]))
