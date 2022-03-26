class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Start,End = 0,len(numbers)-1
        while(Start < End):
            Res = numbers[Start]+numbers[End]
            if(Res == target):
                return [Start+1,End+1]
            elif(Res > target):
                End -= 1
            else:
                Start += 1
