from datetime import datetime
from functools import wraps


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time for running {func.__name__} : {end-start}")
        return result

    return wrapper
