# Execution time decorator
import functools
import time

def time_this(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time {func.__name__}(): {end - start}')
        return result
    return wrapper
