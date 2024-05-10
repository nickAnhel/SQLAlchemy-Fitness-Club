import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload, joinedload

from database import engine, session_factory, Base
from models import User, Office, Subscription, Service, ServiceTypes


def create_tables() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


# Users
class UserRepository:
    @staticmethod
    def create_user(first_name: str, last_name: str, email: str) -> None:
        with session_factory() as session:
            user = User(first_name=first_name, last_name=last_name, email=email)
            session.add(user)
            session.commit()

    @staticmethod
    def get_users():
        with session_factory() as session:
            query = (
                select(User)
                .options(selectinload(User.subscriptions))
            )
            users = session.execute(query).scalars().all()

            # users = session.query(User).all()
            return users

    @staticmethod
    def get_user(user_id: int):
        with session_factory() as session:
            query = (
                select(User)
                .filter_by(id=user_id)
                .options(selectinload(User.subscriptions))
            )
            user = session.execute(query).scalar()

            # user = session.query(User).filter_by(id=user_id).scalars()
            return user

    @staticmethod
    def change_user_email(user_id: int, new_email: str):
        with session_factory() as session:
            stmt = (
                update(User)
                .values(email=new_email)
                .filter_by(id=user_id)
            )
            session.execute(stmt)

            # user = session.query(User).filter_by(id=user_id).scalars()
            # user.email = new_email  # type: ignore

            session.commit()

    @staticmethod
    def change_user_phone_number(user_id: int, new_phone_number: str):
        with session_factory() as session:
            stmt = (
                update(User)
                .values(phone=new_phone_number)
                .filter_by(id=user_id)
            )
            session.execute(stmt)

            # user = session.query(User).filter_by(id=user_id).scalars()
            # user.phone = new_phone  # type: ignore

            session.commit()

    @staticmethod
    def delete_user(user_id: int):
        with session_factory() as session:
            stmt = delete(User).filter_by(id=user_id)
            session.execute(stmt)

            # user = session.query(User).filter_by(id=user_id)
            # user.delete()

            session.commit()


# Services
class ServiceRepository:
    @staticmethod
    def create_services():
        with session_factory() as session:
            for service_type in ServiceTypes:
                service = Service(service_type=service_type)
                session.add(service)

            session.commit()

    @staticmethod
    def create_service(service_type: ServiceTypes):
        with session_factory() as session:
            service = Service(service_type=service_type)
            session.add(service)
            session.commit()

    @staticmethod
    def get_services():
        with session_factory() as session:
            query = (
                select(Service)
                .options(selectinload(Service.offices))
            )
            services = session.execute(query).scalars().all()

            # services = session.query(Service).all()
            return services

    @staticmethod
    def get_service(service_id: int):
        with session_factory() as session:
            query = (
                select(Service)
                .filter_by(id=service_id)
                .options(selectinload(Service.offices))
            )
            service = session.execute(query).scalar()

            # service = session.query(Service).filter_by(id=service_id).scalars()
            return service

    @staticmethod
    def delete_service(service_id: int):
        with session_factory() as session:
            stmt = delete(Service).filter_by(id=service_id)
            session.execute(stmt)

            # service = session.query(Service).filter_by(id=service_id)
            # service.delete()

            session.commit()


# Offices
class OfficeRepository:
    @staticmethod
    def create_office(address: str, phone_number: str, services: list[ServiceTypes]):
        with session_factory() as session:
            office = Office(address=address, phone_number=phone_number)

            for service_type in services:
                query = select(Service).filter_by(service_type=service_type)
                service = session.execute(query).scalar()
                office.services.append(service)  # type: ignore

            session.add(office)
            session.commit()

    @staticmethod
    def get_offices():
        with session_factory() as session:
            # query = select(Office).options(selectinload(Office.services))
            query = (
                select(Office)
                .options(selectinload(Office.services))
                .options(selectinload(Office.subscriptions))
            )
            offices = session.execute(query).scalars().all()

            # offices = session.query(Office).all()
            return offices

    @staticmethod
    def get_office(office_id: int):
        with session_factory() as session:
            query = (
                select(Office)
                .filter_by(id=office_id)
                .options(selectinload(Office.services))
                .options(selectinload(Office.subscriptions))
            )
            office = session.execute(query).scalar()

            # office = session.query(Office).filter_by(id=office_id).scalars()
            return office

    @staticmethod
    def add_service_to_office(office_id: int, service_type: ServiceTypes):
        with session_factory() as session:
            query = (
                select(Service)
                .filter_by(service_type=service_type)
                .options(selectinload(Service.offices))
            )
            service = session.execute(query).scalar()

            office = session.query(Office).filter_by(id=office_id).scalar()
            office.services.append(service)  # type: ignore
            session.commit()

    @staticmethod
    def delete_office(office_id: int):
        with session_factory() as session:
            stmt = delete(Office).filter_by(id=office_id)
            session.execute(stmt)

            # office = session.query(Office).filter_by(id=office_id)
            # office.delete()

            session.commit()


# Subscriptions
class SubscriptionRepository:
    @staticmethod
    def create_subscription(user_id: int, office_id: int, end_date: datetime.datetime):
        with session_factory() as session:
            subscription = Subscription(user_id=user_id, office_id=office_id, end_date=end_date)
            session.add(subscription)
            session.commit()

    @staticmethod
    def get_subscriptions():
        with session_factory() as session:
            query = (
                select(Subscription)
                .options(joinedload(Subscription.user))
                .options(joinedload(Subscription.office))
            )
            subscriptions = session.execute(query).scalars().all()

            # subscriptions = session.query(Subscription).all()
            return subscriptions

    @staticmethod
    def get_subscription(subscription_id: int):
        with session_factory() as session:
            query = (
                select(Subscription)
                .filter_by(id=subscription_id)
                .options(joinedload(Subscription.user))
                .options(joinedload(Subscription.office))
            )
            subscription = session.execute(query).scalar()

            # subscription = session.query(Subscription).filter_by(id=subscription_id).scalars()
            return subscription
