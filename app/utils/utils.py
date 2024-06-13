from random import randint
def generate_random_int(left: int = 0, right: int = 10**100) -> int:
    """Generate a random integer within the given range."""
    return randint(left, right)
