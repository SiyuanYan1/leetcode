# 如果当前节点有右子树，那么中序的下一个节点就是右子树的最左节点。如图中的b，中序的下一个是h。只需沿着右子树，一直往左下找就行。
# 如果没有右子树
# 如果它是父节点的左子节点，那么中序的下一个就是它的父节点，如图中的f，下一个是c
# 如果是父节点的右子节点，就需要往上找父节点，直到找到一个节点x，x是它的父节点的左子节点，这样的话x的父节点就是要找的节点。例如图中i，沿着往上找到b是a的左子节点，那么a就是i中序的下一个。如果找不到，例如图中g，a已经没有父节点，所以g没有下一个中序节点。


# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right: #如果有右子树，则找右子树的最左节点
            node=pNode.right
            while node.left:
                node=node.left
            return node
        else:
            while pNode.next: #没右子树，则找第一个当前节点是父节点左孩
                if pNode.next.left==pNode:
                    return pNode.next
                else:
                    pNode=pNode.next
            return None