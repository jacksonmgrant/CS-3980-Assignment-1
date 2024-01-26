#fib.py
#By Jackson Grant

from functools import lru_cache
import time

def timer(func):
    """Print the runtime of the decorated function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Finished in {run_time:.8f}s: f({args[0]}) -> {value}")
        return value
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    """Return the nth fibonacci number."""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
if __name__ == "__main__":
    fib(100)