# 问题: 删除链表中重复的结点
#
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
#
# 思路
#
# 首先构造一个空的头节点（以防出现 1->1 这样的链表，应当返回空），然后有两个指针，pre指向当前已经处理好了的链表，而last指向当前正在处理的节点。
#
# 对于每个节点
#
# 如果它和它后面的值相同，那么就让它一直往后走，直到它和它后面的值不相同，然后把它后面的节点，接到当前处理完链表的后面；
# 如果它和它后面的值不同，就直接接到链表上，然后继续往后找即可

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# pre用来指向处理好的节点
#last指向当前正在处理的节点
#在最前面接一个空node是为了 能够让last从第一个pHead开始判断，否则不能判断 1->1->null中的重复node
class Solution:
    def deleteDuplication(self, pHead):
        if (not pHead) or (not pHead.next):
            return pHead
        head=ListNode(0)
        head.next=pHead
        pre=head
        last=head.next
        while last is not None:
            if last.next and last.next.val!= last.val:
                pre=pre.next
                last=last.next
            else:
                while last.next and last.val==last.next.val:
                    last=last.next
                pre.next=last.next
                last=last.next
        return head.next



