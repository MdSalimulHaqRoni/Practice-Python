userVal = int(input("Enter a number to find factorial: "))
number = 1
factorial = 1
while number <= userVal:
    factorial *= number
    number += 1
print("Factorial of a number is:", factorial)
