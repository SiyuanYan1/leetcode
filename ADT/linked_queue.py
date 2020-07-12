from node import Node

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def reset(self):
        self.__init__()

    def append(self, item):
        new_node = Node(item, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def serve(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        temp = self.front.item
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp

