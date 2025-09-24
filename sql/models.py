from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

import os

print(os.getcwd())

"""
connect = "<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>"
#postgresql - use pgadmin4
postgresql_db_url = "postgresql://<username>:<password>@<hostname>:<port>/<database>"

#mysql
mysql_db_url ="mysql://<username>:<password>@<hostname>:<port>/<database>"

#oracle
oracle_db_url= "pracle://<username>:<password>@<hostname>:<port>/<database>"

"""

# sqllite
db_url = (
    "sqlite:///database.db"  # /// Relative path where we running,  //// absolute path
)

# engine = create_engine("sqlite+pysqlite:///:memory:")
engine = create_engine(db_url, echo=True)
Base = declarative_base()

# Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)
