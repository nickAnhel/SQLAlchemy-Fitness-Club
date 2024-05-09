from queries.core import create_tables, add_user, get_user_by_id, get_users, update_user_first_name


create_tables()
add_user("Nick", "Anhel", "asd@localhost")
add_user("Aduch", "Gold", "dsa@localhost")
print(get_users())
print(get_user_by_id(user_id=1))
print(get_user_by_id(user_id=2))

update_user_first_name(user_id=1, new_first_name="Nik")
print(get_user_by_id(user_id=1))
