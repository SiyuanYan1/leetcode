from my_stack import Stack
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

    def __iter__(self):
        return PreorderIteratorStack(self.root)

    def __len__(self):
        return self.len_aux(self.root)
    def len_aux(self,current):
        if current is None:
            return 0
        else:
            return 1+self.len_aux(current.left)+self.len_aux(current.right)

    def get_leaves(self):
        a_list=[]
        self.get_leaves_aux(self.root,a_list)
        return a_list
    def get_leaves_aux(self,current,a_list):
        if current is not None:
            if self.is_leave(current):
                a_list.append(current.item)
            else:
                self.get_leaves_aux(current.left,a_list)
                self.get_leaves_aux(current.right,a_list)

    def is_leave(self,current):
        return current.left is None and current.right is None



    def add(self, item, location_bitstring):
        bit_iter=iter(location_bitstring)
        self.root=self.add_aux(self.root,item,bit_iter)

    def add_aux(self, current, item, bitstring_iterator):
        if current is None:
            current = TreeNode()
        try:
            bit = next(bitstring_iterator)
            if bit == "0":
                current.left = self.add_aux(current.left, item, bitstring_iterator)
            elif bit == "1":
                current.right = self.add_aux(current.right, item, bitstring_iterator)
            else:
                raise ValueError("Invalid bit")
        except StopIteration:
            current.item = item
        return current
    def print_preorder(self):
        self.print_preorder_aux(self.root)
    def print_preorder_aux(self,current):
        if current is not None:
            print(current)
            self.print_preorder_aux(current.left)
            self.print_preorder_aux(current.right)




class PreorderIteratorStack:

    def __init__(self, root):
        self.current=root
        self.stack=Stack(1000000)
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
        return current


if __name__ == '__main__':
    tree=BinaryTree()
    tree.add(1,"")
    tree.add(2,"0")
    tree.add(3,"1")
    tree.add(20, "00")
    # tree.add(40, "01")
    # tree.add(56, "10")
    # tree.add(89, "11")


    # for item in tree:
    # #     print(item)
    # tree.print_preorder()
    # for item in tree:
    #     print(item,end=",")
    # print(tree.get_leaves())