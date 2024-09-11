# In this code:
NUMBER=[12,34,0,12]
N1=[bin(x) for x in NUMBER]# N1 = [bin(x) for x in NUMBER]: This is a list comprehension that iterates over each element x in the NUMBER
# list. For each element x, the function bin(x) is called, 
# which converts the integer x into its binary representation (in string form, prefixed with 0b).

print(N1)

# print(N1): This prints the resulting list N1 that contains the binary representation of each number from the NUMBER list.

# Output:
# The binary representation of the numbers will be:

# bin(12) → '0b1100'
# bin(34) → '0b100010'
# bin(0) → '0b0'
# bin(12) → '0b1100'