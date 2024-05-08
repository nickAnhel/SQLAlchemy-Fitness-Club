import datetime
import enum
from sqlalchemy import ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column

from database import BaseModel


class Services(enum.Enum):
    GYM = "Gym"
    POOL = "Pool"
    SAUNA = "Sauna"
    YOGA = "Yoga"
    CROSSFIT = "Crossfit"


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', NOW())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', NOW())"), onupdate=func.now  # type: ignore
    )


class Office(BaseModel):
    __tablename__ = "offices"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str]
    services: Mapped[list[Services]]


class Subscription(BaseModel):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    office_id: Mapped[int] = mapped_column(ForeignKey("offices.id", ondelete="SET NULL"))
    start_date: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', NOW())"))
    end_date: Mapped[datetime.datetime]
