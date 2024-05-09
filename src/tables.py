from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey, func

# from enums import Services

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("email", String),
    Column("phone", String),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, server_default=func.now(), server_onupdate=func.now()),  # type: ignore
)


offices = Table(
    "offices",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("address", String),
    Column("phone", String),
    # Column("services", Services),
)


subscriptions = Table(
    "subscriptions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("office_id", Integer, ForeignKey("offices.id", ondelete="CASCADE")),
    Column("start_date", DateTime, server_default=func.now()),
    Column("end_date", DateTime),
)
