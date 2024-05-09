import datetime
from queries.orm import create_tables, add_user, get_user_by_id, get_users, update_user_first_name, add_office, add_subscription

from enums import Services


create_tables()

add_user("Nick", "Anhel", "asd@localhost")
add_user("Aduch", "Gold", "dsa@localhost")

add_office("123 Main Street", "123-456-7890", Services.GYM)

add_subscription(1, 1, datetime.datetime.now() + datetime.timedelta(days=30))

print(get_users())
print(get_user_by_id(user_id=1))
print(get_user_by_id(user_id=2))

update_user_first_name(user_id=1, new_first_name="Nik")
print(get_user_by_id(user_id=1))
