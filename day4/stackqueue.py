"""用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。"""



"""解题思路：一个stack处理push，另一个处理pop，"""
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if len(self.stack1)==0 and len(self.stack2)==0:
            print("Nothing to pop")
            return
        if len(self.stack2)==0:
            while(len(self.stack1)!=0):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()