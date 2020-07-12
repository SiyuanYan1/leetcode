class Node:
    def __init__(self, key, item, left=None, right=None):
        self.key = key
        self.value = item
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def isLeaf(self):
        return self.right is None and self.left is None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __str__(self):
        return self.inorder()

    def __getitem__(self, key):
        if self.root is None:
            raise KeyError()
        else:
            return self.search(key, self.root)

    def __setitem__(self, key, value):
        self.root=self.set_aux(self.root,key,value)
    def set_aux(self,current,key,value):
        if current is None:
            current=Node(key,value)
        elif key<current.key:
            current.left=self.set_aux(current.left,key,value)
        elif key>current.key:
            current.right=self.set_aux(current.right,key,value)
        else:
            current.value=value
        return current

    def __contains__(self, key):
        return self.contain_aux(self.root,key)
    def contain_aux(self,current,key):
        if current is None:
            return False
        elif current.key==key:
            return True
        elif key<current.key:
            return self.contain_aux(current.left,key)
        else:
            return self.contain_aux(current.right,key)

    def getitem(self,key):
        return self.getitem_aux(self.root,key)

    def getitem_aux(self,current,key):
        if current is None:
            raise KeyError("Key not found")
        elif current.key==key:
            return current.value
        elif key<current.key:
            return self.getitem_aux(current.left,key)

        else:
            return self.getitem_aux(current.right,key)   #return 用来从if curret.key==key那里return回来的value一直能return 回stack最上层




    def insert(self,key,item):
        self.root=self.insert_aux(self.root,key,item)

    def insert_aux(self,current,key,item):
        if current is None:
            current=Node(key,item)
        elif key<current.key:
            current.left=self.insert_aux(current.left,key,item)
        elif key>current.key:
            current.right=self.insert_aux(current.right,key,item)
        else:
            raise ValueError("Duplicate Item")
        return current

    def inorder(self):
        return self.inorder_aux(self.root)

    def inorder_aux(self, current):
        if current is None:
            return ""
        else:
            strin = str(self.inorder_aux(current.left)) + " "
            strin += str(current) + " "
            strin += str(self.inorder_aux(current.right)) + " "
            return strin


BST = BinarySearchTree()
BST[5] = "hello"
BST[5] = "goodbye"
BST[15] = "dubs fo lyf"
BST[10] = "hooray"
# print(5 in BST)
# print(10 in BST)
# print(BST.getitem(5))
# print(BST.getitem(10))
# print(BST.getitem(2))
# for item in BST:
#     print(item,end=",")
print(BST.inorder())
# print(BST)
# print(BST[15])
# print(BST[99])




