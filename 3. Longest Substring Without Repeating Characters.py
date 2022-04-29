class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenSet = set()
        MaxSubString = 0
        sLen = len(s)
        Ind = 0
        PrevInd = 0
        while(Ind < sLen):
            if(s[Ind] not in seenSet):
                seenSet.add(s[Ind])
                Ind += 1
            else:
                seenSet.remove(s[PrevInd])
                PrevInd += 1
            if(len(seenSet) > MaxSubString):
                MaxSubString = len(seenSet)
        return MaxSubString
