from queries.core import create_tables, add_user


create_tables()
add_user("admin", "admin@localhost")
