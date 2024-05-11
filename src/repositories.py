import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload, joinedload

from database import engine, session_factory, Base
from models import User, Office, Membership, Service, ServiceTypes


def create_tables() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


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
            query = select(User).options(selectinload(User.memberships))
            users = session.execute(query).scalars().all()

            # users = session.query(User).all()
            return users

    @staticmethod
    def get_user(user_id: int):
        with session_factory() as session:
            query = select(User).filter_by(id=user_id).options(selectinload(User.memberships))
            user = session.execute(query).scalar_one_or_none()

            # user = session.query(User).filter_by(id=user_id).scalars()
            return user

    @staticmethod
    def change_user_email(user_id: int, new_email: str):
        with session_factory() as session:
            stmt = update(User).values(email=new_email).filter_by(id=user_id)
            session.execute(stmt)

            # user = session.query(User).filter_by(id=user_id).scalars()
            # user.email = new_email  # type: ignore

            session.commit()

    @staticmethod
    def change_user_phone_number(user_id: int, new_phone_number: str):
        with session_factory() as session:
            stmt = update(User).values(phone_number=new_phone_number).filter_by(id=user_id)
            session.execute(stmt)

            # user = session.query(User).filter_by(id=user_id).scalars()
            # user.phone = new_phone  # type: ignore

            session.commit()

    @staticmethod
    def delete_user(user_id: int):
        with session_factory() as session:
            # stmt = delete(User).filter_by(id=user_id)
            # session.execute(stmt)

            user = session.query(User).filter_by(id=user_id).first()
            session.delete(user)

            session.commit()


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
            query = select(Service).options(selectinload(Service.offices))
            services = session.execute(query).scalars().all()

            # services = session.query(Service).all()
            return services

    @staticmethod
    def get_service(service_id: int):
        with session_factory() as session:
            query = select(Service).filter_by(id=service_id).options(selectinload(Service.offices))
            service = session.execute(query).scalar_one_or_none()

            # service = session.query(Service).filter_by(id=service_id).scalars()
            return service

    @staticmethod
    def delete_service(service_id: int):
        with session_factory() as session:
            # stmt = delete(Service).filter_by(id=service_id)
            # session.execute(stmt)

            service = session.query(Service).filter_by(id=service_id).first()
            session.delete(service)

            session.commit()


class OfficeRepository:
    @staticmethod
    def create_office(address: str, phone_number: str, services: list[ServiceTypes]):
        with session_factory() as session:
            office = Office(address=address, phone_number=phone_number)

            for service_type in services:
                query = select(Service).filter_by(service_type=service_type)
                service = session.execute(query).scalar_one_or_none()
                office.services.append(service)  # type: ignore

            session.add(office)
            session.commit()

    @staticmethod
    def get_offices():
        with session_factory() as session:
            # query = select(Office).options(selectinload(Office.services))
            query = select(Office).options(selectinload(Office.services)).options(selectinload(Office.memberships))
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
                .options(selectinload(Office.memberships))
            )
            office = session.execute(query).scalar()

            # office = session.query(Office).filter_by(id=office_id).scalars()
            return office

    @staticmethod
    def add_service_to_office(office_id: int, service_type: ServiceTypes):
        with session_factory() as session:
            query = select(Service).filter_by(service_type=service_type).options(selectinload(Service.offices))
            service = session.execute(query).scalar()

            office = session.query(Office).filter_by(id=office_id).scalar()
            office.services.append(service)  # type: ignore
            session.commit()

    @staticmethod
    def delete_office(office_id: int):
        with session_factory() as session:
            # stmt = delete(Office).filter_by(id=office_id)
            # session.execute(stmt)

            office = session.query(Office).filter_by(id=office_id).first()
            session.delete(office)

            session.commit()


class MembershipRepository:
    @staticmethod
    def create_membership(user_id: int, office_id: int, end_date: datetime.datetime):
        with session_factory() as session:
            membersip = Membership(user_id=user_id, office_id=office_id, end_date=end_date)
            session.add(membersip)
            session.commit()

    @staticmethod
    def get_memberships():
        with session_factory() as session:
            query = select(Membership).options(joinedload(Membership.user)).options(joinedload(Membership.office))
            membersips = session.execute(query).scalars().all()

            # membersips = session.query(Membership).all()
            return membersips

    @staticmethod
    def get_membership(membership_id: int):
        with session_factory() as session:
            query = (
                select(Membership)
                .filter_by(id=membership_id)
                .options(joinedload(Membership.user))
                .options(joinedload(Membership.office))
            )
            membersip = session.execute(query).unique().scalar_one_or_none()

            # membersip = session.query(Membership).filter_by(id=membersip_id).scalars()
            return membersip

    @staticmethod
    def delete_membership(membership_id: int):
        with session_factory() as session:
            stmt = delete(Membership).filter_by(id=membership_id)
            session.execute(stmt)
            session.commit()
