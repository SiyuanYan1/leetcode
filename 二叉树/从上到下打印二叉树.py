# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]， 用bfs按层遍历
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        queue=[root]
        res=[]
        while queue:
            res.append(queue[0].val)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
        return res




