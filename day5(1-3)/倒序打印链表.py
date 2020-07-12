# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, node):
        if node is None:
            return []
        arr=[]
        while node is not None:
            arr.append(node.val)
            node=node.next
        return arr[::-1]
