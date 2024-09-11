# def pali(number):
#     l=number[::1]
#     if l==number:
#         print("it is palindrome")
#     else:
#         print("it is not a palindrome")
# # number=input("enter the number")
# number=100
# pali(number)

def pali(number):
    l = number[::-1]  # Reverse the string
    if l == number:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

number = input("Enter the number: ")
pali(number)
