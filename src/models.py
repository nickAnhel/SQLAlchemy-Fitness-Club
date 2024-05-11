import enum
import datetime
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str]
    phone_number: Mapped[str | None]

    memberships: Mapped[list["Membership"]] = relationship(
        back_populates="user",
        cascade="all, delete",
    )

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())  # type: ignore
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now())  # type: ignore


class ServiceTypes(enum.StrEnum):
    GYM = "Gym"
    POOL = "Pool"
    SAUNA = "Sauna"
    YOGA = "Yoga"
    CROSSFIT = "Crossfit"


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_type: Mapped[ServiceTypes]

    offices: Mapped[list["Office"]] = relationship(
        back_populates="services",
        secondary="office_services",
    )


class Office(Base):
    __tablename__ = "offices"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(unique=True)
    phone_number: Mapped[str]

    services: Mapped[list["Service"]] = relationship(
        back_populates="offices",
        secondary="office_services",
    )
    memberships: Mapped[list["Membership"]] = relationship(
        back_populates="office",
        cascade="all, delete",
    )


class OfficeService(Base):
    __tablename__ = "office_services"

    office_id: Mapped[int] = mapped_column(
        ForeignKey("offices.id"),
        primary_key=True,
    )
    service_id: Mapped[int] = mapped_column(
        ForeignKey("services.id"),
        primary_key=True,
    )


class Membership(Base):
    __tablename__ = "memberships"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    office_id: Mapped[int] = mapped_column(ForeignKey("offices.id"))
    user: Mapped["User"] = relationship(
        back_populates="memberships",
    )
    office: Mapped["Office"] = relationship(
        back_populates="memberships",
    )

    start_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())  # type: ignore
    end_date: Mapped[datetime.datetime]
