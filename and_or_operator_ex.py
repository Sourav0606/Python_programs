user_name, age=input("Entr your name and age:").split(",")
age=int(age)
first_letter=user_name[0]
if (first_letter == "a" or first_letter =="A") and age >=10:
    print("you can watch movie")
else:
    print("sorry, you can't watch movie")