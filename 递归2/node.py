
class Node:

    def __init__(self, item=None, link=None):
        self.item = item
        self.next = link

    def __str__(self):
        return str(self.item)


def print_structure(node):
    current_node = node
    print("[", end="")
    while current_node is not None:
        print(current_node, end=", ")
        current_node = current_node.next
    print("]")


if __name__ == "__main__":
    # FIT1045 --> FIT1008 --> FIT2004
    # first        second     third
    node3 = Node('FIT2004')
    node2 = Node('FIT1008', node3)
    node1 = Node('FIT1045', node2)
    print_structure(node1)

    alone = Node()
    print(alone)
