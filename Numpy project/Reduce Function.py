import functools
def add_two_value(num1, num2):
    return num1 + num2
list1 = [2, 3, 4, 6, 5, 7 , 9]
result = functools.reduce(add_two_value, list1)
print(result)