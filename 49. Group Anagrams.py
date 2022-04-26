class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        SortMap = collections.defaultdict(list)
        for word in strs:
            subArr = [0]*26
            for ch in word:
                subArr[ord(ch)-97] += 1
            SortMap[tuple(subArr)].append(word)
        return [Val for Val in SortMap.values()]
