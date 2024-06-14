from fastapi import APIRouter, HTTPException
import json
import string
from utils.utils import *


router = APIRouter(prefix="/random")


@router.get("/")
def get_root() -> dict:
    """Return a random float between 0 and 1."""
    return {"float": random_float()}


@router.get("/int")
def get_random_int() -> dict:
    """Return a random integer."""
    return {"int": random_int()}


@router.get("/int/{left}/{right}")
def get_random_in_range(left: int, right: int) -> dict:
    """Return a random integer within the given range."""
    if left > right:
        raise HTTPException(status_code=400, detail="Invalid range")
    return {"int": random_int(left, right)}


@router.get("/char")
def generate_random_char() -> dict:
    """Get a random ASCII character."""
    return {"char": random_choice(string.ascii_letters)}


@router.get("/coinflip")
def toss_coin() -> dict:
    """Simulate a coin toss and return the result."""
    return {"result": random_choice(["Heads", "Tails"])}


@router.get("/select/{options}")
def get_random_option(options: str) -> dict:
    """Select a random option from the given list."""
    options_list = json.loads(options)
    if not options_list:
        raise HTTPException(status_code=400, detail="Invalid options")
    return {"selected": random_choice(options_list)}


@router.get("/color")
def get_color() -> dict:
    """Select a random hex color."""
    hex_color = "#" + \
        "".join([random_choice('0123456789ABCDEF') for _ in range(6)])
    return {"color": hex_color}


@router.get("/user")
def get_user() -> User:
    """Generate a random user with name, email, and password."""
    return random_user()


@router.get("/password/{length}")
def get_password(length: int) -> dict:
    """Generate a random password of a specified length."""
    return {"password": random_password(length=length)}
