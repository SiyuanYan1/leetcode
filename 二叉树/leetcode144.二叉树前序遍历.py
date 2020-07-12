# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        a_list=[]
        self.p_aux(root,a_list)
        return a_list
    def p_aux(self,current,a_list):
        if current is not None:
            a_list.append(current.val)
            self.p_aux(current.left,a_list)
            self.p_aux(current.right,a_list)

"""基于栈的迭代方法"""
class Solution1:
    def preorderTraversal(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return res


