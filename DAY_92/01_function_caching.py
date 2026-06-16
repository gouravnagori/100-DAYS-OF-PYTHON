

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    # complex computation
    return (n*89) - 37 + n

print(fx(3))
print(fx(1))
print(fx(1))
print(fx(6))
print(fx(7))
print(fx(8))
print(fx(2))
print(fx(8))

