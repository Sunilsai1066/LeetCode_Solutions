class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Prev = None
        Curr = head
        while(Curr != None):
            Next = Curr.next
            Curr.next = Prev
            Prev = Curr
            Curr = Next
        return Prev
