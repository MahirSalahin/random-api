from fastapi import FastAPI
from routers.random import random_router

app = FastAPI()
app.include_router(random_router)

@app.get("/")
def get_home() -> dict:
    """Return the API home page with available routes."""
    routes = {
        "/": "Description of the api",
        "/random": "Get a random float between 0 and 1.",
        "/random/int": "Get a random integer",
        "/random/range/{left}/{right}": "Get a random integer within the specified range.",
        "/random/char": "Get a random ASCII character.",
        "/random/coinflip": "Simulate a coin toss and get the result.",
        "/random/choice/{options}": "Select a random option from the given list.",
        "/random/color": "Select a random hex color.",
        "/random/user": "Generate a random user with name, email, and password.",
        "/random/password/{length}": "Generate a random password of a specified length.",
    }
    meta = {
        "api_version": "1.0",
        "docs": "https://github.com/MahirSalahin/random_api"
    }
    return {"routes": routes, "meta": meta}
