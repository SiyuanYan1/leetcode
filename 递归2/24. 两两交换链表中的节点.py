# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_recursion:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        else:
            tmp=head.next
            head.next=self.swapPairs(tmp.next)
            tmp.next=head
        return tmp


class Solution:#迭代法
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        c=dummy
        while c.next and c.next.next:
            a,b=c.next,c.next.next
            c.next=b
            a.next=b.next
            b.next=a
            c=c.next.next
        return dummy.next

