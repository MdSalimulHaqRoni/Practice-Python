def maximum(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2
num1 = (input("Enter first number: "))
num2 = (input("Enter second number: "))
print("The maximum number is:",maximum(num1, num2))
