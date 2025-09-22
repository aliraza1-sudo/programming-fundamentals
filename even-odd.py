v = int(input("Enter a number :"))
even_count = 0
odd_count = 0
for i in range(1,  v + 1) :
    if i % 2 == 0 :
        print (i, "is even")
        even_count += 1
    else :
        print (i , "is odd")
        odd_count += 1 
print ("Total even are", even_count )
print ("Total odd are ", odd_count)

    