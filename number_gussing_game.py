import random
winning_number=random.randint(1,100)
guess = 1
user_number=int(input("Enter any number you want to guess: "))
game_over = False

while not game_over :
    if user_number == winning_number :
        print(f"you win, and guess this number in {guess} times")
        game_over = True
    else :
        if user_number < winning_number :
            print("too low")
            #guess += 1
            #user_number = int(input("guess again: "))
        else :
            print("too high")
            #guess += 1
            #user_number = int(input("guess again: "))
        guess += 1   #
        user_number = int(input("guess again: "))   #

        #after dry run###