import datetime

from models import ServiceTypes
from repositories import (
    create_tables,
    UserRepository,
    ServiceRepository,
    OfficeRepository,
    MembershipRepository,
)


def main():
    create_tables()

    print("=====USERS=====")

    # Create users
    UserRepository.create_user("Nick", "Anhel", "nick@mail.com")
    UserRepository.create_user("Aduch", "Gold", "aduch@mail.com")
    UserRepository.create_user("Dmitr", "Moisey", "moisey@mail.com")

    # Get all users
    print("Get all users")
    print(
        UserRepository.get_users(),
        sep="\n",
    )

    # Get user by id
    print("\nGet user by id")
    print(
        UserRepository.get_user(user_id=1)
    )

    # Change user email
    print("\nChange user email")
    print(
        UserRepository.get_user(user_id=1)
    )
    UserRepository.change_user_email(user_id=1, new_email="hello@mail.com")
    print(
        UserRepository.get_user(user_id=1)
    )

    # Change user phone number
    print("\nChange user phone number")
    # Change user phone number
    print("\nChange user phone number")
    print(
        UserRepository.get_user(user_id=1)
    )
    UserRepository.change_user_phone_number(user_id=1, new_phone_number="123-456-7890")
    print(
        UserRepository.get_user(user_id=1)
    )

    # Delete user
    print("\nDelete user")
    UserRepository.create_user("Test", "Testik", "test@mail.com")
    print(
        "Before",
        *UserRepository.get_users(),
        sep="\n",
    )
    UserRepository.delete_user(user_id=4)
    print(
        "After",
        *UserRepository.get_users(),
        sep="\n",
    )

    print("=====USERS=====")

    print("=====SERVICES=====")

    # Create all available services
    ServiceRepository.create_services()

    # Get all services
    print("Get all services")
    print(
        *ServiceRepository.get_services(),
        sep="\n",
    )

    # Get service by id
    print("\nGet service by id")
    print(
        ServiceRepository.get_service(service_id=1),
    )

    # Delete service by id
    # print("\nDelete service by id")
    # print(
    #     "Before",
    #     *ServiceRepository.get_services(),
    #     sep="\n",
    # )
    # ServiceRepository.delete_service(service_id=3)
    # print(
    #     "After",
    #     *ServiceRepository.get_services(),
    #     sep="\n",
    # )

    print("=====SERVICES=====")

    print("=====OFFICES=====")

    # Create offices
    OfficeRepository.create_office("123 Main Street", "123-456-7890", [ServiceTypes.GYM, ServiceTypes.SAUNA])
    OfficeRepository.create_office("234 Main Street", "234-567-8901", [ServiceTypes.POOL, ServiceTypes.CROSSFIT])

    # Get all offices
    print("Get all offices")
    print(
        *OfficeRepository.get_offices(),
        sep="\n",
    )

    # Get office by id
    print("\nGet office by id")
    print(
        OfficeRepository.get_office(office_id=1),
    )

    # Add service to office
    print("\nAdd service to office")
    print(
        "Before\n",
        OfficeRepository.get_office(office_id=1),
    )
    OfficeRepository.add_service_to_office(office_id=1, service_type=ServiceTypes.YOGA)
    print(
        "After\n",
        OfficeRepository.get_office(office_id=1),
    )

    # Delete office by id
    # print("\nDelete office by id")
    # print(
    #     "Before",
    #     *OfficeRepository.get_offices(),
    #     sep="\n"
    # )
    # OfficeRepository.delete_office(office_id=2)
    # print(
    #     "After",
    #     *OfficeRepository.get_offices(),
    #     sep="\n"
    # )

    print("=====OFFICES=====")

    print("=====MEMBERSHIPS=====")

    # Create memberships
    MembershipRepository.create_membership(1, 1, datetime.datetime.now() + datetime.timedelta(days=30))
    MembershipRepository.create_membership(1, 2, datetime.datetime.now() + datetime.timedelta(days=60))
    MembershipRepository.create_membership(2, 1, datetime.datetime.now() + datetime.timedelta(days=20))
    MembershipRepository.create_membership(3, 2, datetime.datetime.now() + datetime.timedelta(days=90))

    # Get all memberships
    print("Get all memberships")
    print(
        *MembershipRepository.get_memberships(),
        sep="\n",
    )

    # Get membership by id
    print("\nGet membership by id")
    print(
        MembershipRepository.get_membership(membership_id=1),
    )

    # Delete membership by id
    # print("\nDelete membership by id")
    # print(
    #     "Before",
    #     *MembershipRepository.get_memberships(),
    #     sep="\n",
    # )
    # MembershipRepository.delete_membership(membership_id=2)
    # print(
    #     "After",
    #     *MembershipRepository.get_memberships(),
    #     sep="\n",
    # )

    print("=====MEMBERSHIPS=====")


    # UserRepository.delete_user(1)
    OfficeRepository.delete_office(1)

if __name__ == "__main__":
    main()
