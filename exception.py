number=10
while True:
    try:
        num=int(input("enter the number"))
        if num<number:
            raise ValueError
        elif num>number:
            raise ValueError
        break
    except ValueError:
        print("enter the the small value")
        print()
    except ValueError:
        print("enter the big number")
        print()
print("good")