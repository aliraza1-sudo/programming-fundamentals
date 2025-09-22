import math
num1 = float (input("Enter first number :"))
num2 = float (input("Enter second number :"))
print ("Available operations are +, -, /, *")
operation = input("Enter operation :")
if operation == "+" :
    result = num1 + num2
    print ("Result :", result)
elif operation == "-" :
    result = num1 - num2
    print ("Result :", result)
elif operation == "*" :
    result = num1 * num2
    print ("Result :", result)
elif operation == "/" :
    if not num2 == 0 :
        result = num1 / num2
        print ("Result :", result)
    else :
        print ("ERROR : cannot divided by zero")
else :
    print ("Invalid option! Please choose +, -, /, * ")



