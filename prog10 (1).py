print ("==== Inputting and Displaying Faculty Data (Class with Constructor)==== \n\n")

class Faculty:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary
        
    def display(self):
        print ("\nName of Faculty:",self.name)
        print ("Subject:",self.subject)
        print ("Salary (in Rs.):",self.salary)
    
    def greet(self):
        print ("\nThank you for providing the information! Have a great Day...",self.name)
        
    def salaryEvaluation(self):
        if self.salary >= 10000:
            print ("Status: Good")
        else:
            print ("Status: Bad")
        

f1 = Faculty("Pratigya Sinha", "PAI", 15000)
f1.display()
f1.salaryEvaluation()
f1.greet()
