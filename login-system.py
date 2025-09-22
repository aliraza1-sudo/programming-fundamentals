username = "aliraza"
password = "ali123"
attempt = 3
while attempt > 0 :
    use = input ("Enter username :")
    pas = input ("Enter password :")
    if use == (username) and pas == (password) :
        print ("Login successful")
    else :
        attempt -= 1
        print("Access denied")
        print("You left with", attempt, "chances")
        if attempt == 0 :
            print ("too  many attempts. Account locked")

