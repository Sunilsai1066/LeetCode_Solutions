class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        Count = 0
        #[1,2,2,3]
        Start,End = 0,len(people)-1
        while(Start <= End):
            if(Start == End):
                Count += 1
                Start += 1
                End -= 1
            elif(people[Start]+people[End] > limit):
                Count += 1
                End -= 1
            else:
                Count += 1
                Start += 1
                End -= 1
        return Count
