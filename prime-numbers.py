# checks whether given numb is prime or not 
num = int(input("Enter number :"))
while num % 1 == num :
    while num % num == 1 :
        print ("It is prime")
print ("It is not prime")
