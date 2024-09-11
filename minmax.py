# Write a short Python function, minmax(data), that takes a sequence of
#  one or more numbers, and returns the smallest and largest numbers, in the
#  form of a tuple of length two. Do not use the built-in functions min or
#  max in implementing your solution.

def minmax(data):
    min=max=data[0]
    for val in data[1:]:
        if val<min:
            min =val
        if val>max:
            max=val
    return (max,min)

print(minmax([1,0,6,98,4,2,6,2,4,6,2]))

# using min and max function

number=[1,0,6,98,4,2,6,2,4,6,2]
print(min(number))
print(max(number))