# Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the positive integers smaller than n.
def sumsquare(n):
    count=0
    result=0
    for i in range(n+1):
        i=i*i
        result=result+i
        count+=1
    return result

ans=int(input("enter the number"))
print(sumsquare(ans))

#using comprehension

sum1=([i*i for i in range(1,5+1)])
print(sum(sum1))
