def divisiblebythree(array):

    s=sum(array) 
    if s%3==0:
        return 1
    return 0

array=list(map(int,input().split()))
print(divisiblebythree(array))