from functools import lru_cache


@lru_cache(maxsize=256)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print(f'Count fibonnaci for {n} egal {str(result)}')
        return result