
from models import User, engine
from sqlalchemy.orm import sessionmaker
import random



Session= sessionmaker(bind=engine)
session= Session()

names= ["andrew","Iron man","John Doe", "Shahswat"]
ages= [20,30,40,21,22,23,30,60]

# for x in range(20):
#     user = User(name=random.choice(names),age=random.choice(ages))
#     session.add(user)
# session.commit()

#query all user by age (ascending)
users=session.query(User).order_by(User.age).all()
users=session.query(User).order_by(User.age.desc()).all()
# SELECT * FROM User ORDER BY name , age; 
users=session.query(User).order_by(User.age,User.name).all() # if same age than dort by name

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")


# SELECT * FROM User WHERE age>=25;

users = session.query(User).filter(User.age>25).all()
# SELECT * FROM User WHERE age>=25 AND name='Shashwat';
users = session.query(User).filter(User.age>25,User.name =="Shashwat").all()

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")

#another way
users = session.query(User).filter_by(age=25).all
#users = session.qurey(User).filter_by(age=>25).all # dont work with conditinal

users = session.query(User).where(user.age >= 30).all()

# SELECT * FROM User WHERE age>=25 OR name='Shashwat';
from sqlalchemy import or_

#users = session.query(User).where(or_(User.age <= 30,User.name=="shashwat")).all()
users = session.query(User).where((User.age <= 30)|(User.name=="shashwat")).all()
for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")

from sqlalchemy import not_ ,and_
users = session.query(User).where(not_(User.age>25)).all()

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")

users =session.query(User).where(
    or_(
        not_(User.name == "Iron man"),
        and_(User.age >35,
        User.age <60
        )
    )
).all