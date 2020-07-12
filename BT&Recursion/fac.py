# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

def factorial(n):
    return factorial_aux(n,1)

def factorial_aux(n,result):
    if n==0:
        return result
    else:
        return factorial(n-1,result*n)


