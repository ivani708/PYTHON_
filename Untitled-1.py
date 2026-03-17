f1=open("text1","w")
f1.write("hello\n")
f1.write("good morning\n")
f.close()

#read this file
f1.open("text1","r")
print(f1.read())
f1.close 

#update the file
f1.open("text1","a")
f1.write("gd eveng")
f1.close()

# # x=2
# # y=4

# # print(x/y)
 
# # try:
# #     print(x/y)
# # except Exception as e:
# # print("You can't divide by zero")
# # print("hello")    


# x=2
# y=4


# print(x+y)
 
# try:
#     print(x+y)
# # except Exception as e:
# except ZeroDivisonError:
#     print("You can't divide by zero")
# except TypeError:
#     print("only number")
# except Exception:
#     print("something went wrong")
    
# print("hello")    e

#create nd write in file

f1=open("text1","w")
f1.write("hello\n")
f1.write("good morning\n")
f1.close()

#read this file
f1.open("text1","r")
print(f1.read())
f1.close 

#update the file
f1.open("text1","a")
f1.write("gd eveng")
f1.close()

f1=open("text1","r")
f2=open("text2","w")

for data in f1:
    f2.write(data)

f1.close()
f2.close()
#rd=read binary file
#use seek(0) for pointer the read file from starting 
#wd=write binary file





