# Write a pseudo-code description of a function that reverses a list of n
#  integers, so that the numbers are listed in the opposite order than they
#  were before, and compare this method to an equivalent Python function
#  for doing the same thing.

def reverser(L,n):
    left=0
    right=n-1
    while left<right:
        L[left],L[right]=L[right],L[left]
        
        left=left+1
        right=right-1
    return L


L=[1,2,3,4,5,6,7,9]
n=len(L)
print(reverser(L,n))

#using built in function
L.reverse()
print(L) ### this will give the original becouse the list L is already reverssd by the function reverser
print(L[::-1])  # this function will reveres the output of the above code
