age=int(input("Please enter your age: "))
if 0<=age<=3:
    print("For this age group Ticket is 'FREE'")
elif 3<age<=10:
    print("For this age group Ticket amount is 'RS.150'")
elif 10<age<=60:
    print("For this age group Ticket amount is 'RS.250'")
else:
    print("For this age group Ticket amount is 'RS.200'")