class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head == None):return False
        Slow = Fast = head
        while Fast and Fast.next:
            Slow = Slow.next
            Fast = Fast.next.next
            if(Slow == Fast):
                return True
        return False
