class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Slow = Fast = head
        def ReturnNode(Slow,Fast):
            if(Slow == Fast):
                return Slow
            while(Slow):
                Slow = Slow.next
                Fast = Fast.next
                if(Slow == Fast):
                    return Slow
        while Fast and Fast.next:
            Slow = Slow.next
            Fast = Fast.next.next
            if(Slow == Fast):
                return ReturnNode(head,Fast)
        return None
