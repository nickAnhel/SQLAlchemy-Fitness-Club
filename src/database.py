from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

import config


engine = create_engine(
    config.DB_URL,
    echo=True,
)

session_factory = sessionmaker(bind=engine)


class BaseModel(DeclarativeBase):
    pass
