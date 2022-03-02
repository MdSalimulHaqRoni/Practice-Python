import random
guess = random.randint(1, 100)
print("Please pick a number b/w 1 to 100")
guess_no = 0
while True:
    select = int(input(":"))
    if select < guess:
        print("guess high")
    else:
        if select > guess:
            print("guess low")
        elif select == guess:
            print("Congratulations, you guess it")
            print("You guess it in, ", guess_no)
            break
            guess_no+=1