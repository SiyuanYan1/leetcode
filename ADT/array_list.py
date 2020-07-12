from referential_array import build_array


class List:

    def __init__(self, max_capacity):
        assert max_capacity > 0, "Max capacity has to be positive"
        self.count = 0
        self.array = build_array(max_capacity)

    def length(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.array)

    def add(self, item):
        has_space_left = not self.is_full()
        if has_space_left:
            self.array[self.count] = item
            self.count += 1
        return has_space_left

    def to_string(self):
        ans = "["
        for i in range(self.count):
            ans += str(self.array[i])
            ans += ', '
        ans += ']'
        return ans

    def delete(self, index):
        valid_index = 0 <= index < self.count
        if valid_index:
            for i in range(index, self.count-1):
                self.array[i] = self.array[i+1]
            self.count -= 1
        return valid_index


if __name__ == "__main__":
    a_list = List(1000)
    a_list.add(5)
    a_list.add("Hello")
    a_list.add(10)
    print(a_list.to_string())
    a_list.delete(1)
    print(a_list.to_string())