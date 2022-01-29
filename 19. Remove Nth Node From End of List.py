class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Fast = Slow = head
        for i in range(n):
            Fast = Fast.next
        if(not Fast):return head.next
        while(Fast.next != None):
            Slow,Fast = Slow.next,Fast.next
        Slow.next = Slow.next.next
        return head
