from node import Node
from node import print_structure


class List:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return False

    def reset(self):
        self.__init__()

    def __len__(self):
        return self._length(self.head)

    def _length(self, current):
        if current is None:
            return 0
        else:
            return 1+self._length(current.next)


    def __contains__(self, item):
        return self._contains_aux(self.head,item)

    def _contains_aux(self, current, item):
        if current is None:
            return False
        else:
            return current.item==item or self._contains_aux(current.next,item)


    def _get_node(self, index):
        assert 0 <= index < len(self), "Index out of bounds"
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def insert(self, index, item):
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)
        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self._get_node(index - 1)
            node.next = Node(item, node.next)

    def __iter__(self):
        return MyLinkedListIterator(self.head)

    def delete(self, index):
        if self.is_empty():
            raise IndexError("The list is empty")
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
        else:
            node = self._get_node(index-1)
            node.next = node.next.next

    def copy(self):
        new_list=List()
        self.copy_aux(self.head,new_list)
    def copy_aux(self,current,a_list):
        if current is not None:
            self.copy_aux(current.next,a_list)
            a_list.insert(0,current.item)


class MyLinkedListIterator:

    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item_required = self.current.item
            self.current = self.current.next
            return item_required

    def __iter__(self):
        return self


def main():
    a_list = List()
    a_list.insert(0, -2)
    a_list.insert(0, 2)
    a_list.copy()
    # a_list.insert(0, 3)
    # a_list.insert(0, 5)

    for item in a_list:
        print(item, end=", ")
    # print("")
    # print(len(a_list))
    # print(-2 in a_list)
    # print(6 in a_list)


if __name__ == "__main__":
    main()


