import time
import requests

from functools import lru_cache
from functools import wraps

def benchmark(original):
    @wraps(original)
    def wrapper(*args, **kwargs):
        start   = time.time()
        result  = original(*args, **kwargs)
        end     = time.time()
        latency = end - start
        print(f'{latency=}')
        return result
    return wrapper

@benchmark
@lru_cache
def sivan(number):
    while number < 5000000:
        number += 1
    return number

@benchmark
@lru_cache
def fetchGoogle():
    result = requests.get("https://www.google.com/")
    return result

fetchGoogle()
fetchGoogle()
fetchGoogle()
fetchGoogle()
fetchGoogle()
fetchGoogle()
fetchGoogle()
fetchGoogle()
