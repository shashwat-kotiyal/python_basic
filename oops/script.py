#every thing is an object in python
# name ="Danny"
# age =29
#
# print(type(name))
# print(type(age))
#
# #different object have different behivour
# print(name.upper())

#we can create our own object from that clases

    #A class is the blueprint for creating objects, it defines  attribute or data store information about object, method define  object action and behivour
class Dog:
    def __init__(self,name,bread): #run only when obj is intanciated
        self.name=name
        self.bread= bread
    #self refer to instance or specific obj of class itself,
    #parameter is used to , refers to specific object and method inside class
    def bark(self):
        print("Whoof Whoof")


dog1=Dog("bruce", "scottish terrier")  # creating dog object
dog1.bark()

dog2 = Dog("snoopy", "labradour")
dog2.bark()

class Owner:
    def __init__(self,name, address, contact_number ):
        self.name=name
        self.address= address
        self.contact_number = contact_number
