from database import engine, session_factory, BaseModel
from models import User


def create_tables():
    BaseModel.metadata.drop_all(bind=engine)
    BaseModel.metadata.create_all(bind=engine)


def add_user(name: str, email: str):
    with session_factory() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
