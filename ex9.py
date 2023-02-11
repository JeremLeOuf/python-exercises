import random

num = random.randint(1,9)

while True:
    try:
        guess = int(input("Guess the number... "))
        if guess > 9:
            print("Number must be between 1 and 9.")
        elif guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        elif guess == num:
            print("GOTCHA!")
            break
        
    except Exception as e:
        print(e)
        break
