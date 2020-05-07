import time
import math
import random

start_time = time.time()

cache = {}

def build_lookup_table():
	for i in range(50000):
		cache[i] = math.factorial(i)

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    v = math.pow(x, y)
    # v = math.factorial(v)
    if v not in cache:
    	cache[v] = math.factorial(v)

    v = cache[v]
    v //= (x + y)
    v %= 982451653

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")