class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        Len = len(nums)
        if(Len == 1):
            return
        def Reverse(Lis,Start,End):
            while(Start < End):
                Lis[Start],Lis[End] = Lis[End],Lis[Start]
                Start += 1
                End -= 1
        k %= Len
        Reverse(nums,0,Len-1)
        Reverse(nums,0,k-1)
        Reverse(nums,k,Len-1)
