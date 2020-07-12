# def fac(n):
#     if n==0:
#         return 1
#     else:
#         return n*fac(n-1)

def fac(n):
    return fac_aux(n,1)
def fac_aux(n,result):
    if n==0:
        return 1
    else:
        return fac_aux(n-1,result*n)

