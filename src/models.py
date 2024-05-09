import datetime
import enum
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Services(enum.Enum):
    GYM = "Gym"
    POOL = "Pool"
    SAUNA = "Sauna"
    YOGA = "Yoga"
    CROSSFIT = "Crossfit"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str]
    phone: Mapped[str | None]

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())  # type: ignore
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now())  # type: ignore


class Office(Base):
    __tablename__ = "offices"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str]
    services: Mapped[Services]


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    office_id: Mapped[int] = mapped_column(ForeignKey("offices.id", ondelete="CASCADE"))
    start_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())  # type: ignore
    end_date: Mapped[datetime.datetime]
