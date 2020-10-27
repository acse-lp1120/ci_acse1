from functools import lru_cache
__all__ = ['my_sum', 'factorial'] #add factorial here to make it visible


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot

@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9, checks if previous factorial has already been introduced, such that if we do 10 factorial before, if we call 11 factorial, just multiply 10 factorial by 11
def factorial(n):
    return n * factorial(n-1) if n else 1