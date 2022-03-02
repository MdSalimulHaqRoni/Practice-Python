x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Before swapping: ")
print("Value of x: ", x, "and y: ", y)
x = x + y
y = x - y
x = x - y
print("After swapping: ")
print("Value of x: ", x, "and y: ", y)