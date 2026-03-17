# Understanding if-else and if-elif ladder

a = int (input ("Enter value of a: "))
b = int (input ("Enter value of b: "))

if a > b :
    print ("a is greater than b")
elif b > a :
    print ("b is greater than a")
else :
    print ("a and b are equal...")
    
if a >= 90 :
    print ("Topper")
elif a >= 70 :
    print ("Good")
elif a >= 50 :
    print ("Average")
else :
    print ("Fail")