from fastapi import FastAPI, Request, routing
from routers.random import router as randoom_router

app = FastAPI()
app.include_router(randoom_router)

@app.get("/")
def get_home(request: Request) -> dict:
    """Return the API home page with available routes."""
    routes = {}
    for route in request.app.routes:
        if isinstance(route, routing.APIRoute):
            routes[route.path] = route.name
    meta = {
        "api_version": "1.0",
        "docs": "https://github.com/MahirSalahin/random_api"
    }
    return {"routes": routes, "meta": meta}