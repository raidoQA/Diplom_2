from faker import Faker

faker = Faker()
fakerRU = Faker(locale='ru_Ru')


def create_email_user_random():
    email = faker.free_email()
    return email


def create_user_pass_random():
    password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_user_name_random():
    name = faker.name()
    return name