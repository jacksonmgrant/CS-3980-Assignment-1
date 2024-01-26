#fib.py
#By Jackson Grant

import functools

@lru_cache
@timer
def fib(n: int) -> int:
    """Return the nth fibonacci number."""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
if __name__ == "__main__":
    print(fib(100))