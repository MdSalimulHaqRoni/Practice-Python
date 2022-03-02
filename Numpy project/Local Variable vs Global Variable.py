x = 100
def some_functiom():
    global x
    x = x + 150
    print("Inside:", x)
some_functiom()
print("Outside: ", x)
