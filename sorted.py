enter=input("enter the number")
number=[]
for i in enter.split():
    try:
        number.append(i)
    except ValueError:
        print(f"'{i}' its not valid")
# print(number)

new=sorted(list(set(number)))
print(new)

enter=input("enter the number")
number=[]
for i in enter.split():
    try:
        number.append(i)
    except ValueError:
        print("enter the valid number")

final=print(tuple(set(number)))


