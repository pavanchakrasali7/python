# number=[1,2,3,4,5,6,7]
# def check(number):
#     if number%2==0:
#         return True
#     return False

# check_even=map(check,number)
# ch=list(check_even)
# print(ch)

# number=[1,2,3,4,5,6,7]
# def check(number):
#     if number%2==0:
#         return True
#     return False

# check_even=filter(check,number)
# ch=list(check_even)
# print(ch)


# vowels=['q','e','r','t','a','e']
# def vowel(vowels):
#     vo=['a','e','i','o','u']
#     return True if vowels in vo else False
# fil=filter(vowel,vowels)
# check=tuple(fil)
# print(check)

number=[1,2,3,4,5,6,7,8,9,0]
check=filter(lambda x:(x%2==0),number)
chec=list(check)
print(chec)