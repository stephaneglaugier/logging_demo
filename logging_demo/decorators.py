import logging
import timeit
from functools import wraps
from typing import Callable, Coroutine


def timed(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        logging.info(
            f"{func.__name__} took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper


def timed_coroutine(crtn: Coroutine):
    @wraps(crtn)
    async def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = await crtn(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        logging.info(
            f"{crtn.__name__} took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper
