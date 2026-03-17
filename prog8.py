print ("=====  OOPs in Python  =====\n\n")
class Student:
    def data(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print ("\nEntered name:",self.name)
        print ("Entered age:",self.age)
        
s1 = Student()
s1.data('Pratigya Sinha', '36')
s1.display()