def power(x,N):
    if N==0:
        return 1
    else:
        value=power(x,N//2)
        if N%2==0:
            return value*value
        else:
            return value*value*x



print(power(2,10))