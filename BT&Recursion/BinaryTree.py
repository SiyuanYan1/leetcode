class TreeNode:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.item)

class BinaryTree:
    def __init__(self):
        self.root=None
    def is_empty(self):
        return self.root is None
    def add(self):
        return None

    def print_preorder(self):
        self.preorder_aux(self.root)
    def preorder_aux(self,current):
        if not current:
            print(current)
            self.preorder_aux(current.left)
            self.preorder_aux(current.right)
    def __len__(self):
        return self.len_axu(self.root)

    def len_axu(self,current):
        if current is None:
            return 0
        else:
            return 1+self.len_axu(current.left)+self.len_axu(current.right)

    def get_leaves(self):
        a_lsit=[]
        self.get_leaves_aux(self.root,a_lsit)
    def get_leaves_aux(self,current,alist):
        if current is not None:
            if self.is_leaf(current):
                alist.append(current)
            else:
                self.get_leaves_aux(current.left,alist)
                self.get_leaves_aux(current.right,alist)
    def is_leaf(self,current):
        return current.left is None and current.right is None

class Stack:

class PreOrderIteratorStack:
    def __init__(self,root):
        self.current=root
        self.stack=Stack()
        self.stack.push(root)
    def __iter__(self):
        return self
    def __next__(self):
        if self.stack.is_empty():
            raise StopIteration
        current=self.stack.pop()
        if current.right is not None:
            self.stack.push(current.right)
        if current.left is not None:
            self.stack.push(current.left)
        return current.item

