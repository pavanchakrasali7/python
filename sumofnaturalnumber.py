# def sum(n):
#     count=0
#     result=0
#     while count<=n:
#         result+=count
#         count+=1
        
#     return result
# print(sum(5))


# Generator 
def factors(n):
    k=1
    while k* k < n:
        if n%k==0:
            yield k
            yield n//k
            k+=1
        if k *k==n:
            yield k
    return k
print(list(factors(5)))