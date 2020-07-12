def bi_search(arr,target):
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]<target:
            lo=mid+1
        elif arr[mid]>target:
            hi=mid-1
        else:
            return arr[mid]
    return -1

aList = [5,10,15,20,25,30,35,40,45,50,55]
print(bi_search(aList,10))


"""recursion bi search"""
def bi_search2(arr,target,lo,hi):
    mid=(lo+hi)//2
    if arr[mid]==target:
        return arr[mid]
    if lo==hi:
        return -1
    if arr[mid]<target:
        return bi_search2(arr,target,mid+1,hi)
    else:
        return bi_search2(arr,target,lo,mid-1)
aList = [5,10,15,20,25,30,35,40,45,50,55]
print(bi_search2(aList,20,0,len(aList)))
