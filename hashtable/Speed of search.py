Speed of search
---------------

Linear search through an array

Network caching

Memoization--expensive calculation


Indexing
--------
Alice: 30
Bob:   40
Charlie: 20
Dave: 20
Beej: 20

"Show me all the people who are age 30"

What do I want to look up by?  <-- that's the key

30: [Alice]
40: [Bob]
20: [Charlie, Dave, Beej]


Given a list of records, need to conver into a hashtable first
THEN we can do quick lookups


Removing Duplicates
-------------------

h = {}

for in in data:
	# Have we seen this data before
	if h[i]: #same as checking for existence if the set
		continue

	# We've seen it now:
	h[i] = True # same as adding to a set

	print(i)

#Slow calculation caching
"""
cache = {}

def fib(n):
	if n <= 1:
		return n

	if n not in cache:
		cache[n] = fib(n-1) + fib(n-2)

	return cache[n]

for i in range(100):
	print(fib(i))
"""

"""
import math

cache = {}

def build_lookup_table():
	for i in range(1, 1000):
		inv_square_root(i)

def inv_square_root(n):
	if n not in cache:
		cache[n] = 1 / math.sqrt(n)

	return cache[n]

for i in range(1, 6):
	print(inv_square_root(i))

"""

"""
d = {
	"foo": 12,
	"bar": 17,
	"qux": 2
}

# Sort by key:
items = list(d.items())

print(items)

items.sort() # sort by key first the value second

print(items)

for i in items:
	print(f'{i[0]}: {i[1]}')

# Sort by Value:
items = list(d.items())

print(items)

items.sort(key=lambda e: e[1]) # sort by key first the value second

print(items)

for i in items:
	print(f'{i[0]}: {i[1]}')
"""

encode_table = {
	'A': 'H', 'B': 'Z', 'C': 'Y', 'D': 'W', 'E': 'O','F': 'R', 'G': 'J', 'H': 'D', 'I': 'P', 'J': 'T',
	'K': 'I', 'L': 'G', 'M': 'L', 'N': 'C', 'O': 'E', 'P': 'X', 'Q': 'K', 'R': 'U', 'S': 'N', 'T': 'F', 'U': 'A',
	'V': 'M', 'W': 'B', 'X': 'Q', 'Y': 'V', 'Z': 'S'
}

decode_table = {}

for k,v in encode_table.items():
	decode_table[v] = k

def encode(s):
	r = ""

	for c in s:
		r += encode_table[c]

	return r

print(encode("ABCD"))

print(decode("HZYW"))