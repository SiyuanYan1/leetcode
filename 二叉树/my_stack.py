from referential_array import build_array


class Stack:

    def __init__(self, max_capacity):
        assert max_capacity > 0, 'eh?'
        self.array = build_array(max_capacity)
        self.count = 0
        self.top = -1

    def __len__(self):
        return self.count

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) >= len(self.array)

    def reset(self):
        self.count = 0
        self.top = -1

    def push(self, item):
        assert not self.is_full(), "No space!"
        self.array[self.count] = item
        self.count += 1
        self.top += 1

    def pop(self):
        assert not self.is_empty(), "Nothing to pop"
        item = self.array[self.top]
        self.top -= 1
        self.count -= 1
        return item

    def peek(self):
        assert not self.is_empty(), "Nothing to look at"
        return self.array[self.top]


if __name__ == "__main__":
    a_stack = Stack(100)
    a_stack.push(1)
    a_stack.push(2)
    print(a_stack.pop())
    print(a_stack)













