#Basic Approach - 2 Pass
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Count = 0
        CountCheck = head
        while(CountCheck != None):
            Count += 1
            CountCheck = CountCheck.next
        NewList = None
        if(Count == 1): return NewList
        Ind = Count//2
        Count = -1
        Prev = -1
        ResNode = None
        while(head != None):
            Count += 1
            if(Count == Ind):
                head = head.next
            else:
                Node = ListNode(head.val)
                if(NewList == None):
                    NewList = Node
                    ResNode = NewList
                else:
                    NewList.next = Node
                    NewList = NewList.next
                head = head.next
        return ResNode
