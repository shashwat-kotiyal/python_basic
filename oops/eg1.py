class Employee:
    salary_raised = 0.5  # class variable(static variable /attribute (funcyion or varibale)) attribute belong to class not instance to a class
    count = 0

    def __init__(self, Name, Id, Salary):
        self.Name = Name
        self._Id = Id
        self._Salary = Salary  # instance veriable
        Employee.count += 1
        # Employee.count = Employee.count + 1

    def email(self):
        return f"{self.Name}@email.com"

    @property
    def email1(self):
        return f"{self.Name}@email.com"

    @property
    def Salary(self):
        return f"{self._Salary}"

    @Salary.setter
    def Salary(self, value):
        self._Salary = value
        # return self.Salary

    def __str__(self):
        return f" Employe_Name-{self.Name} salary is {self.Salary}"  # by default 1st it will call _str_ 1st if object is print if no _str_ that check fpr _repr_

    def __repr__(self):
        return f"Employee({self.Name},{self.Salary},{self._Id})"


emp1 = Employee("bijay", 1, 400000)
print(emp1.email())
print(emp1.Salary)
emp1.Salary = 560000
print(emp1.Salary)

# print(emp1.email1())

print(emp1.email1)

print(emp1)
print(emp1.count)
print(emp1.Name)
emp2 = Employee("Shashwat", 2, 5000000)
print(emp2.__repr__())
print(emp2.__str__())  #
print(emp2)
print(emp1.Name)
print(emp2.Name)
print(emp1.count)
print(emp2.count)
print(Employee.count)
emp3 = Employee("Amit", 3, 300000)
print(emp3)
print(emp3.count)
print(emp1.count)
print(dir(print))
