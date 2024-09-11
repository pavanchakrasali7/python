import random
data=sorted(random.randint(1,20) for _ in range(1,10))
target=int(input("enter the number to check whether the number is present in the list or not"))
print(data)
def binary(data,target):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        if target<data[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

found=binary(data,target)

if found:
    print(f"{target} is present in the list")
else:
    print(f"{target} not present in the list")