
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session =sessionmaker(bind=engine) #tells where we are making transaction ,which database
session = Session()    #return actual session object

user = User(name="John Doe", age=30)
user_2 = User(name="Aman",age=40)
user_3 = User(name="Shashwat",age=35)
user_4 = User(name="Bijay",age=45)

session.add(user)
session.add_all([user_3,user_4])
session.commit()

users=session.query(User).all()

print(users)
print(users[0])
user=users[0]
print(user.id)
print(user.name)
print(user.age)

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")


users= session.query(User).filter_by(id=1).all()

print(users)

user= session.query(User).filter_by(id=1).one_or_none()
print(user)

user.name ="A different name"
print(user.name)


session.commit() #it will change 

session.delete(user)
