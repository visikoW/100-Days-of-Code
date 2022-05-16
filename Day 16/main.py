
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

Vinycius = Student("Vinycius", "Florencio", 2022)

print(Vinycius.graduationyear)
print(Vinycius.printname())