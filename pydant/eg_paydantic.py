from pydantic import validate_call
from pydantic.v1 import EmailStr


@validate_call
def create_user(first_name: str, last_name: str, age:int)->dict:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    return{
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
    }

user: dict = create_user("Corey","Schafer",38)
#print(user1)

from pydantic import BaseModel, EmailStr, field_validator

#Pydantic is a Python library for data validation and settings management using Python type hints

class User(BaseModel):  ## data validation, serialization, dynamic defaults, not builtin, slow
    name: str  # Required string field
    email: str  # EmailStr
    acc_id: int  # Required integer field
    is_active: bool = True  # Optional field with default value
    age: int = None
    # age: int | None = None   #cleaner | syntax instead of Optional

    @field_validator("acc_id")  # custom validators
    def validate(cls, value):
        if value <= 0:
            raise ValueError(f"account id must be positive:{value}")
        return value

    # Validate email format (using Pydantic V2 syntax)
    @field_validator("email")
    def check_email(cls, value):
        if '@' not in value:
            raise ValueError("email should contain @")
        return value.lower()


def basic():
    user_data = {
        'name': 'Jack',
        'email': 'jack@gmail.com',
        'acc_id': 1234
    }
    user1 = User(**user_data)
    print(user1.name)
    print(user1.email)
    print(user1.acc_id)
    #provide type hint
    #data validation
    ### Invalid input (triggers ValidationError)
    from pydantic import ValidationError
    try:            #put in try to proceed further on error
        User(name="Bob", email="bob.example.com", acc_id=17)
        #user2 =User(name='brajesh', email='brajesh@gmail.com', acc_id='sds')
        # #inbuild validation classes
        # user3 =User(name='brajesh', email='brajeshgail.com', acc_id=1234)
        # print(user3.name)
        # #custom validation
        # user4 =User(name='brajesh', email='brajesh@gmail.com', acc_id=-10)
    except ValidationError as e:
        print(e.errors())


    ### json serialization
    # Convert to JSON
    #user1_json_str =user1.json()   #depricated
    user1_json_str =user1.model_dump_json()
    print(user1_json_str)

    # Convert to dictionary
    #user1_json_obj = user1.dict()  #depriciated
    user1_json_obj = user1.model_dump()
    print(user1_json_obj)


    # model validation
    # JSON string → Model
    json_str = '{"name": "Alice", "email": "alice@mas","acc_id": 12,"age": 30}'
    user5 = User.model_validate_json(json_str)
    print(user5)  # User(name='Alice', age=30)

    #Parse a dictionary (loaded from JSON) into a model
    # data = {"name": "Bob", "age": 25}
    # user = User.model_validate(data)  # Dict → Model

    from dataclasses import dataclass
    @dataclass                  #no data validation, serialization, builtin, only static defaults, fast
    class Employee:
        name: str
        email: str
        acc_id: int


def model():
    from pydantic import model_validator
    class UserProfile(BaseModel):
        username: str
        password: str
        confirm_password: str

        @model_validator(mode='after')
        def check_password(self):
            if self.password != self.confirm_password:
                raise ValueError("password and confirm password not matched")
            return self

    #Cross-Field Validation
    #    Ensure dependencies between fields are correct (e.g., start_date < end_date).
    # Post-Processing
    #   Compute derived fields or apply business logic after all data is validated.
    # Model-Level Adjustments
    #   Modify the entire model instance based on combined field values.

    #WHEN USE BEFORE?
    # Data Transformation: Convert legacy field names or formats.
    # Conditional Defaults: Set defaults based on other raw fields.
    # Early Validation: Reject invalid data before type conversion.



if __name__ == "__main__":
#what is pydantic?
#How do you define a basic Pydantic model? Provide an example.
#What are validators in Pydantic, and how do you use them?
#How does Pydantic handle type hints compared to traditional Python type checking?
#difference between data class and pydantic
#7. How does Pydantic handle JSON parsing and serialization?
    basic()

#what is data model_validator, field_validator
    #model()
#What is the difference between BaseModel and BaseSettings in Pydantic?





    pass
