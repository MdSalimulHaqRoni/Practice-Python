'''
def mul_five_times(number):
    return number * 5
result = []
num = [5, 6, 8, 2, 4]
for i in num:
    result.append(mul_five_times(i))
print(result)
Output:[25, 30, 40, 10, 20]
'''

def mul_five_times(number):
    return number * 5
num = [5, 6, 8, 2, 4]
result= list(map(mul_five_times, num))
print(result)