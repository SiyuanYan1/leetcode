# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        else:
            return True if abs(self.getDepth(pRoot.left) - self.getDepth(pRoot.right)) <= 1 else False

    def getDepth(self, current):
        if current is None:
            return 0
        else:
            return 1 + max(self.getDepth(current.left), self.getDepth(current.right))