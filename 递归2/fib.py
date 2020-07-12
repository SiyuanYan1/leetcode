def fib(n):
    return fib_aux(n ,0 ,1)
def fib_aux(n ,before_last ,last):
    if n== 0:
        return before_last
    else:
        return fib_aux(n - 1, last, before_last + last)


print(fib(5))