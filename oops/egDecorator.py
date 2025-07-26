class Employee:
    emp_count=0
    raise_amt= 1.05
    def __init__(self,first_name,last_name,salary):
        self.first_name= first_name
        self.last_name= last_name
        Employee.emp_count +=1

    def email1(self):
        return f"{self.last_name}{self.first_name}@celona.io"

    @property
    def email(self):
        return f"{self.last_name}{self.first_name}@celona.io"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


    @fullname.setter
    def fullname(self,name):
        self.first, self.last = name.strip().split()



emp1= Employee("Anil","kumar",400000)
print(emp1.email1())  #decorater make function behave like attributes
print(emp1.email)

emp1.fullname= "Lokhnath das"

print(emp1.fullname)

print("*"*5+"first calss function"+"*"*5)

# assign onefuntionto other
def square(x):
    return x*x

f=square
print(f(5))

#pass as argument

squares = map(square,[1,2,3,4,5])

print(list(squares))

#return as function
def logger(msg):
    def log():
        print(f"Log: {msg}")

    return log

logger("hi")
abc=logger("bismil")  #its waiting for execution
abc()


print("*"*5+"Closure"+"*"*5)
#A closure is a function object that remembers
# values in enclosing scopes even if those scopes are no longer present