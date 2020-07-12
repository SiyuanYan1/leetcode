import copy


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
#路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.list=[]
        self.wholelist=[]


    def FindPath(self, root, expectNumber):
        if root is None:
            return self.wholelist
        self.list.append(root.val)
        expectNumber-=root.val
        if expectNumber==0 and not(root.left or root.right):
            self.wholelist.append(copy.deepcopy(self.list))
        self.FindPath(root.left,expectNumber)
        self.FindPath(root.right,expectNumber)
        self.list.pop()
        return self.wholelist

