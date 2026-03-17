print ("==== Inputting and Displaying Faculty Data ==== \n\n")

class Faculty:
    def data (self):
        self.name = input ("Faculty Name: ")
        self.subject = input ("Subject assigned: ")
        self.salary = int (input ("Salary obtained (in Rs.): "))
        
    def display(self):
        print ("\nName of the Faculty:",self.name)
        print ("Subject assigned:",self.subject)
        print ("Salary obtained (in INR):",self.salary)
    
    def greet(self):
        print ("\nThank you for providing the information! Have a great Day...",self.name)
        
f1 = Faculty()
f1.data()
f1.display()
f1.greet()

