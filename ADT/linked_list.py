from node import Node
from node import print_structure
class List:
    def __init__(self):
        self.head=None
        self.count=0


    def is_empty(self):
        return self.count==0


    def is_full(self):
        return False

    def reset(self):
        self.__init__()


    def __len__(self):
        return self.count


    def _get_node(self, index):
        assert 0<=index<=self.count, "index out of bound"
        node=self.head
        for _ in range(index):
            node=node.next
        return node


    def insert(self, index, item):
        if index<0:
            index=0
        if index>len(self):
            index=len(self)
        if index==0:
            self.head=Node(item,self.head)
        else:
            node=self._get_node(index-1)
            node.next=Node(item,node.next)
        self.count+=1

    def __iter__(self):
        return MyLinkedListIterator(self.head)


    def delete(self, index):
        if self.is_empty():
            raise IndexError("The list is empty")
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        if index==0:
            self.head=self.head.next
        else:
            node=self._get_node(index-1)
            node.next=node.next.next
        self.count-=1



class MyLinkedListIterator:
    def __init__(self,head):
        self.current=head
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is  None:
            raise StopIteration
        else:
            item=self.current.item
            self.current=self.current.next
            return item






def all_positive(my_list):
    for item in my_list:
        if item < 0:
            return False
    return True


# def maximum_item(my_list):
#     for item in my_list:
#         if max_value < item:
#             max_value = item
#     return max_value


if __name__ == "__main__":
    a_list = List()
    a_list.insert(0, 1)
    a_list.insert(1, 2)
    a_list.insert(0, -5)
    print(all_positive(a_list))










