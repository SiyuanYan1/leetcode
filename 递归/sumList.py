def doSomething(aList):
    n = len(aList)
    if n == 0:
        return 0
    else:
        return aList[0] + doSomething(aList[1:])
L = [10,30,20]
value = doSomething(L)
print(value)
