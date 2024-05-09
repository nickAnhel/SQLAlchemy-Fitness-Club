from database import engine, session_factory, Base
from models import User, Office, Services


def create_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def add_user(first_name: str, last_name: str, email: str):
    with session_factory() as session:
        user = User(first_name=first_name, last_name=last_name, email=email)
        session.add(user)
        session.commit()


def get_users():
    with session_factory() as session:
        users = session.query(User).all()
        return users


def get_user_by_id(user_id: int = 1):
    with session_factory() as session:
        user = session.query(User).filter_by(id=user_id).one_or_none()
        return user


def update_user_first_name(user_id: int, new_first_name: str):
    with session_factory() as session:
        user = session.query(User).filter_by(id=user_id).one_or_none()
        user.first_name = new_first_name
        session.commit()


def add_office(address: str, phone: str, services: Services):
    with session_factory() as session:
        office = Office(address=address, phone=phone, services=services)
        session.add(office)
        session.commit()
