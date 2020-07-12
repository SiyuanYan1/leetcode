from my_stack import Stack


class TreeNode:

    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.item)


class BinaryTree:

    def __init__(self):
        self.root = None

    def __iter__(self):
        return PreorderIteratorStack(self.root)

    def add(self, item, location_bitstring):
        bitstring_iterator = iter(location_bitstring)
        self.root = self.add_aux(self.root, item, bitstring_iterator)

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
                raise ValueError("Invalid bitstring")
        except StopIteration:
            current.item = item
        return current

    def print_preorder(self):
        self._print_preorder_aux(self.root)

    def _print_preorder_aux(self, current):
        if current is not None:
            print(current, end=",")
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)

    def print_inorder(self):
        self._print_inorder_aux(self.root)

    def _print_inorder_aux(self, current):
        if current is not None:
            self._print_inorder_aux(current.left)
            print(current, end=",")
            self._print_inorder_aux(current.right)

    def print_posorder(self):
        self._print_posorder_aux(self.root)

    def _print_posorder_aux(self, current):
        if current is not None:
            self._print_posorder_aux(current.left)
            self._print_posorder_aux(current.right)
            print(current, end=",")


class PreorderIteratorStack:

    def __init__(self, root):
        self.current = None
        self.stack = Stack(1000)
        self.stack.push(root)

    def __iter__(self):
        return self

    def __next__(self):
        if self.stack.is_empty():
            raise StopIteration
        current = self.stack.pop()
        if current.right is not None:
            self.stack.push(current.right)
        if current.left is not None:
            self.stack.push(current.left)
        return current.item


def my_example_tree():
    ans = BinaryTree()
    ans.add(43, "")
    ans.add(31, "0")
    ans.add(64, "1")

    # ans.add(20, "00")
    # ans.add(40, "01")
    # ans.add(56, "10")
    # ans.add(89, "11")
    #
    # ans.add(28, "001")
    # ans.add(33, "010")
    # ans.add(47, "100")
    # ans.add(59, "101")
    return ans


def main():
    a_tree = my_example_tree()
    for item in a_tree:
        print(item, end=",")

if __name__ == "__main__":
    main()







