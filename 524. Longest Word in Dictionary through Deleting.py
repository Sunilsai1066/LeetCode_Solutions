class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res,resLen = "",0
        for word in dictionary:
            if(len(word) >= resLen):
                wordInd,sInd = 0,0
                wLen,sLen = len(word),len(s)
                while(wordInd < wLen and sInd < sLen):
                    if(word[wordInd] == s[sInd]):
                        wordInd += 1
                        sInd += 1
                    else:
                        sInd += 1
                if(wordInd == wLen and wLen > resLen):
                    res,resLen = word,wLen
                elif(wordInd == wLen and wLen == resLen and word < res):
                    res = word
        return res
