def greatest_number(num1, num2) :
    if num1 > num2 :
        return num1
    else :
        return num2
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"greatest number is {greatest_number(a, b)}")