def moveDisks(n, start, end, temp):
    if n==1:
        print("move disk from ",start," to ",end)
    else:
        moveDisks(n-1,start,temp,end)
        print("move disk from ",start," to ",end)
        moveDisks(n-1,temp,end,start)
moveDisks(3,"Start","End","temp")

