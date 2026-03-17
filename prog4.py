name = input ("Enter Student's Name: ")
print ("Entered Name:",(name))
print (type(name))
print ()

marks = int (input ("Enter Student's Marks: "))
print ("Entered Marks:",(marks))
print (type(marks))
print ()

if marks >= 75 :
    print ("Distinction")
elif marks >= 60 :
    print ("First Class")
elif marks >=40 :
    print ("Passed")
else :
    print ("Fail")
