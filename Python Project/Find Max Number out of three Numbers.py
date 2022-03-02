x = int(input("Enter 1st number: "))
y = int(input("Enter 1st number: "))
z = int(input("Enter 1st number: "))
if x>y:
    if x>z:
        print("X is bigger than yz")
    else:
        print("z is bigger than xy")
elif y>x:
    if y>z:
        print("y is bigger than zx")
    else:
        print("z is bigger than xy")