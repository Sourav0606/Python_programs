user_input=input("Enter the number greater then 1 digit: ")
#print(len(user_input))
total=0
i=0 
while i<len(user_input):
    total += int(user_input[i])
    i += 1
print(total)