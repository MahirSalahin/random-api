from fastapi import APIRouter, HTTPException
import random
import json
import secrets
import string
import faker
from utils.utils import *


random_router = APIRouter()

@random_router.get("/random")
def get_root() -> dict:
    """Return a random float between 0 and 1."""
    return {"float": random.random()}


@random_router.get("/random/int")
def get_random_int() -> dict:
    """Return a random integer."""
    return {"int": generate_random_int()}


@random_router.get("/random/range/{left}/{right}")
def get_random_in_range(left: int, right: int) -> dict:
    """Return a random integer within the given range."""
    if left > right:
        raise HTTPException(status_code=400, detail="Invalid range")
    return {"int": generate_random_int(left, right)}


@random_router.get("/random/char")
def generate_random_char() -> dict:
    """Get a random ASCII character."""
    return {"char": random.choice(string.ascii_letters)}


@random_router.get("/random/coinflip")
def toss_coin() -> dict:
    """Simulate a coin toss and return the result."""
    return {"result": random.choice(["Heads", "Tails"])}


@random_router.get("/random/choice/{options}")
def select_randomly(options: str) -> dict:
    """Select a random option from the given list."""
    options_list = json.loads(options)
    if not options_list:
        raise HTTPException(status_code=400, detail="Invalid options")
    return {"selected": random.choice(options_list)}


@random_router.get("/random/color")
def get_color() -> dict:
    """Select a random hex color."""
    hex_colors = [
        "#" + "".join([random.choice('0123456789ABCDEF') for _ in range(6)])]
    return {"color": hex_colors[0]}


@random_router.get("/random/user")
def generate_user() -> dict:
    """Generate a random user with name, email, and password."""
    fake = faker.Faker()
    name = fake.name()
    first_name, last_name = name.split()[0].lower(), name.split()[-1].lower()
    nums = ''
    for _ in range(random.randint(0, 4)):
        nums += str(random.randint(0, 9))
    email = random.choice(
        [f"{first_name}.{last_name}@{fake.free_email_domain()}",
         f"{first_name}.{last_name}{nums}@{fake.free_email_domain()}",
         f"{nums}{first_name}@{fake.free_email_domain()}",
         f"{first_name}{nums}@{fake.free_email_domain()}",
         f"{last_name}{nums}@{fake.free_email_domain()}",
         ])
    user = {
        "name": name,
        "email": email,
        "password": fake.password()
    }
    return user


@random_router.get("/random/password/{length}")
def generate_password(length: int) -> dict:
    """Generate a random password of a specified length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return {"password": password}
