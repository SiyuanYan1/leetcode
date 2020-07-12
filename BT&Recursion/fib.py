# def  fib(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)


def fib(n):
    return fib_aux(n,0,1)

def fib_aux(n,first,second):
    if n==0:
        return first
    else:
        return fib_aux(n-1,second,first+second)