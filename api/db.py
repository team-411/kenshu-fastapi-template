from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

host = "db:3308"
db_name = "todo"
user = "user"
password = "password"

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user,
    password,
    host,
    db_name,
)

ENGINE = create_engine(
    DATABASE,
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
