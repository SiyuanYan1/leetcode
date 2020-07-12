class BinarySearchTreeNode:
    def __init__(self,key,item=None,left=None,right=None):
        self.key=key
        self.item=item
        self.left=left
        self.right=right
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def is_empty(self):
        return self.root is None
    def insert(self,key,item):
        self.root=self.insert_aux(self.root,key,item)
    def insert_aux(self,current,key,item):
        if current is None:
            current=BinarySearchTreeNode(key,item)
        else:
            if key<current.key:
                current.left=self.insert_aux(current.left,key,item)
            elif key>current.key:
                current.right=self.insert_aux(current.right,key,item)
            else:
                raise ValueError("Duplicate Item")
            return current