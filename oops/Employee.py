import datetime
class Employee:
    emp_count=0
    raise_amt= 1.05
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
        Employee.emp_count +=1

    def apply_raise(self):
        self.salary= int(self.raise_amt * self.salary)


    @classmethod
    def set_raise_amt(cls,amount):
        #Print("use to make alternate constructor")
        print("This is a class method")
        print(f"Accessing class_var: {cls.raise_amt}")
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        name,salary = emp_str.split("-")
        return cls(name,salary)

    @staticmethod
    def is_valid_raise(raise_amt):
        return  1<=raise_amt<=1.05

    @staticmethod
    def is_weekday(day):
        if day.weekday() ==5 or day.weekday() ==5:
            return False
        return True

    def __str__(self):
        return f"{self.name}-{self.salary}"

    def __repr__(self):
        return f"Employee({self.name!r},{self.salary})"

    def __len__(self):
        return len(self.name)

print(Employee.emp_count)
emp1 =Employee("prashant", 3600000)
emp2= Employee("mohit", 3200000)

print(Employee.emp_count)
print(emp1.emp_count)
print(emp2.emp_count)


print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

print(Employee.is_valid_raise(0.4))

print(f"{Employee.__dict__}")
#emp1.__dict__ does not contain raise_amt, emp_count
print(f"{emp1.__dict__}")


Employee.set_raise_amt(1.06)
print(Employee.raise_amt)

print("*"*5+"use class method to make alternate constructor"+"*"*5)
emp_str = "saransh-4500000"
emp3 = Employee.from_string(emp_str)
print(emp3.salary)

mydate= datetime.date(2025,7,24)
print(Employee.is_weekday(mydate))

print("*"*5+"Inheritance"+"*"*5)

class DeveloperDummy(Employee):
    raise_amt=1.10
#we can change raise amt in subclass without changing value in parent class
dev1= DeveloperDummy("kavita",500000)
print(Employee.emp_count)
#print(help(dev1))
print(dev1.salary)
dev1.apply_raise()
print(dev1.salary)

class Developer(Employee):
    def __init__(self,name,pay,prg_lang):
        super().__init__(name,pay)
        #Employee.__init__(self,name,pay)   #both super ad this is expectable
        self.prg_lang = prg_lang


dev2 =Developer("ranjit",600000,"c++")

class Manager(Employee):
    def __init__(self,name,pay,employ=None):
        super().__init__(name,pay)
        #Employee.__init__(self,name,pay)   #both super ad this is expectable
        if employ is None:
            self.employ= []
        else:
            self.employee = employ

    def add_employee(self,emp):
        if emp not in self.employ:
            self.employ.append(emp)

    def remove_employee(self,emp):
        if emp in self.employ:
            self.employ.remove(emp)
mag1= Manager("Mohit",1000000,[emp1])

print("*"*5+"isinstance"+"*"*5)
print(isinstance(mag1,Manager))
print(isinstance(mag1,Employee))
print(isinstance(mag1,Developer))

print("*"*5+"issubclass"+"*"*5)
print(issubclass(Developer,Manager))
print(issubclass(Employee,Manager))
print(issubclass(Manager,Employee))

print("*"*5+"specialmethods dunder"+"*"*5)

print(emp1)
print(emp1.__str__())  # For users/readability# For users/readability
print(emp1.__repr__()) # For developers/debugging

# Also, if you just do `print(obj)`, Python uses __str__.
# If __str__ is not defined, it falls back to __repr__.