from fastapi import FastAPI, HTTPException
import random
import json
import math

app = FastAPI()


def generate_random_int(left: int = 0, right: int = math.inf) -> int:
    """Generate a random integer within the given range."""
    return random.randint(left, right)


@app.get("/")
def get_root() -> dict:
    """Return a random float between 0 and 1."""
    return {"random": random.random()}


@app.get("/random_in_range/{left}/{right}")
def get_random_in_range(left: int, right: int) -> dict:
    """Return a random integer within the given range."""
    if left > right:
        raise HTTPException(status_code=400, detail="Invalid range")
    return {"random": generate_random_int(left, right)}


@app.get("/toss_a_coin")
def toss_coin() -> dict:
    """Simulate a coin toss and return the result."""
    return {"result": random.choice(["Heads", "Tails"])}


@app.get("/select/{options}")
def select_randomly(options) -> dict:
    """Select a random option from the given list."""
    options_list = json.loads(options)
    if not options_list:
        raise HTTPException(status_code=400, detail="Invalid options")
    return {"selected": random.choice(options_list)}
