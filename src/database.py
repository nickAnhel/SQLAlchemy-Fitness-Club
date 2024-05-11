import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


engine = create_engine(
    "sqlite:///db.sqlite3",
    # echo=True,
)


session_factory = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        res = []
        for key, value in self.__dict__.items():
            if not key.startswith("_") and not isinstance(value, datetime.datetime):
                res.append(f"{key}={repr(value)}")
        return f"{self.__class__.__name__}({', '.join(res)})"
