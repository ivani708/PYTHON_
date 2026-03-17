# if-else used in for loop

n = int (input ("How many times you want to enter the no.?: "))
print ("Entered n:",n)
print ("Type of entered n:",type(n))
print()
for i in range (n) :
    num = int (input ("Enter number: "))
    print ("Entered num:",num)
    print ("Type of entered num:",type(num))

    if num > 0 :
        print ("Entered no. is positive\n")
    else :
        print ("Entered no. is negative")
