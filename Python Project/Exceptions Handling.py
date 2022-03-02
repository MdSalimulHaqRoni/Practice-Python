a = 10
b = 2
try:
    print("Recourse open:")
    print(a/b)
    n = int(input("Enter any number: "))
except  (ZeroDivisionError, ValueError):
    print("You can not divide a number by zero!")
    print("Something Wrong")
finally:
    print("Recourse close:")

print("Exicute the next line")
