class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Slow = Fast = head
        while Fast and Fast.next:
            Slow = Slow.next
            Fast = Fast.next.next
        return Slow
