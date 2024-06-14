from random import randint, random, choice
from schemas.user import User
from faker import Faker


def random_int(l: int = 0, r: int = 10**3) -> int:
    """Generate a random integer within the given range."""
    return randint(l, r)


def random_float() -> float:
    """Generate a random float number."""
    return random()


def random_choice(options: list):
    """Generate a random choice from a list of options."""
    return choice(options)


def random_password(length=8) -> str:
    """Generate a random password of given length"""
    return Faker().password(length=length)


def random_email(user_name: str = Faker().name()) -> str:
    """Generate a random email address"""
    first_name, last_name = user_name.split(
    )[0].lower(), user_name.split()[-1].lower()

    random_nums = ''.join(str(random_int(r=9))
                          for _ in range(random_int(r=4)))
    email_domain = Faker().free_email_domain()

    return choice(
        [f"{first_name}.{last_name}@{email_domain}",
         f"{last_name}.{first_name}@{email_domain}",
         f"{first_name}.{last_name}{random_nums}@{email_domain}",
         f"{random_nums}{first_name}@{email_domain}",
         f"{first_name}{random_nums}@{email_domain}",
         f"{last_name}{random_nums}@{email_domain}",
         ])


def random_user() -> User:
    user = User()
    user.name = Faker().name()
    user.password = random_password()
    user.email = random_email(user_name=user.name)
    return user
