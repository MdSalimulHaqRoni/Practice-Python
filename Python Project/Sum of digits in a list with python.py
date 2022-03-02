test_list = [15, 20, 25, 30]
print("The original list is:" + str(test_list))
result = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
        result.append(sum)
print("Last integer summation: " + str(result))
