stock = 5
n = int(input("How many iphone do you need?"))
i = 1
while i <= n:
    if i > stock:
        print("Sorry out of stock")
        break
    print("Iphone", i)
    i+=1