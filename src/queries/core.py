from sqlalchemy import insert, select, update  # , text

from database import engine
from tables import metadata, users, offices
from enums import Services


def create_tables():
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)


def add_user(first_name: str, last_name: str, email: str):
    with engine.connect() as conn:
        stmt = insert(users).values(first_name=first_name, last_name=last_name, email=email)
        conn.execute(stmt)
        conn.commit()


def get_users():
    with engine.connect() as conn:
        query = select(users)
        return conn.execute(query).all()


def get_user_by_id(user_id: int = 1):
    with engine.connect() as conn:
        # query = select(User).where(User.id == user_id)
        query = select(users).filter_by(id=user_id)  # .where(User.id == user_id)
        return conn.execute(query).one_or_none()


def update_user_first_name(user_id: int, new_first_name: str):
    with engine.connect() as conn:
        # Raw query
        # stmt = text("UPDATE users SET first_name=:first_name WHERE id=:id")
        # stmt = stmt.bindparams(first_name=new_first_name, id=user_id)

        stmt = update(users).values(first_name=new_first_name).filter_by(id=user_id)  # .where(User.id == user_id)
        conn.execute(stmt)
        conn.commit()


def add_office(address: str, phone: str, services: Services):
    with engine.connect() as conn:
        stmt = insert(offices).values(address=address, phone=phone, services=services)
        conn.execute(stmt)
        conn.commit()
