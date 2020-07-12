# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.cursor = -1

    def push(self, node):
        # write code here
        if self.cursor == -1:
            self.stack1.append(node)
            self.stack2.append(node)
        else:
            if node < self.stack1[self.cursor]:
                self.stack2.append(node)
            else:
                self.stack2.append(self.stack1[self.cursor])
            self.stack1.append(node)
        self.cursor += 1

    def pop(self):
        # write code here
        if self.cursor==-1:
            return None
        res = self.stack1.pop()
        self.stack2.pop()
        self.cursor -= 1
        return res

    def top(self):
        # write code here
        if self.cursor==-1:
            return None
        return self.stack1[self.cursor]

    def min(self):
        # write code here
        if self.cursor==-1:
            return None
        return self.stack2[self.cursor]

