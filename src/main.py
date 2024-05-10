import datetime

from models import ServiceTypes
from crud import (
    create_tables,
    UserRepository,
    ServiceRepository,
    OfficeRepository,
    SubscriptionRepository,
)


create_tables()

# Users
UserRepository.create_user("Nick", "Anhel", "asd@localhost")
# create_user("Aduch", "Gold", "dsa@localhost")

# print(get_users())
# print(get_user_by_id(user_id=1))

# update_user_email(user_id=1, new_email="hello@localhost")
# print(get_user_by_id(user_id=1))

# update_user_phone(user_id=1, new_phone="123-456-7890")
# print(get_user_by_id(user_id=1))

# delete_user(user_id=1)
# print(get_users())


# Services
ServiceRepository.create_services()


# Offices
OfficeRepository.create_office("234 Main Street", "234-567-8901", [ServiceTypes.POOL, ServiceTypes.CROSSFIT])
OfficeRepository.create_office("123 Main Street", "123-456-7890", [ServiceTypes.GYM, ServiceTypes.SAUNA])

# print(get_offices())
# print(get_offices()[0].services)
OfficeRepository.add_service_to_office(1, ServiceTypes.SAUNA)

# print(get_offices())
# delete_office(1)
# print(get_offices())

# Subscriptions
SubscriptionRepository.create_subscription(1, 1, datetime.datetime.now() + datetime.timedelta(days=30))
print(SubscriptionRepository.get_subscriptions())
# s = get_subscription(1)
print(s := SubscriptionRepository.get_subscription(1))
print(s.user)
print(s.office)

# u = get_user(1)
# print(u.subscriptions)
