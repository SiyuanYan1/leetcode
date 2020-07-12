# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:


    def Print(self, pRoot):
            if pRoot == None:
                return []
            else:
                result = []
                node_list = [pRoot]
                row = 1
                while node_list:
                    child_list = []#存储下一行的子节点
                    row_list = []#用来反转
                    for i in node_list:
                        row_list.append(i.val)
                        if i.left != None:
                            child_list.append(i.left)
                        if i.right != None:
                            child_list.append(i.right)
                    node_list = child_list
                    if row %2 == 0:
                        row_list.reverse()
                    result.append(row_list)
                    row += 1
                return result

