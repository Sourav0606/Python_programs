import random
winning_number=random.randint(0,11)
guess_number=int(input("Enter number between 0 to 10: "))
if guess_number==winning_number:
    print("YOU WON !!!!")
elif guess_number > winning_number:
    print("TOO LOW!!")
else:
    print("TOO HIGH!!")

print("winning number was: "+str(winning_number))
     
        
    

    
