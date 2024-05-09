from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

import config


engine = create_engine(
    config.DB_URL,
    echo=True,
)

session_factory = sessionmaker(bind=engine)


Base = declarative_base()
