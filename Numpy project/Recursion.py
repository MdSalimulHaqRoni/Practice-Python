import sys
print("Limit:", sys.getrecursionlimit())
sys.setrecursionlimit(1500)
count = 0
def myfunction():
    global count
    count = count+1
    print("Whats up?", count)
    myfunction()
myfunction()
