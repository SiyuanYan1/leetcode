def func1():
    print(1)
    func2()
    print(4)

def func2():
    func3()
    print(2)

def func3():
    print(3)

if __name__ == '__main__':
    func1()
