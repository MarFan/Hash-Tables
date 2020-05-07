import re
# Implement me.

f = open('robin.txt', 'r')
names_1 = f.read().lower().split()  # List containing 10000 names
f.close()

word_cache = {}

def hist():
	for n in names_1:
		word = re.sub("[^A-Za-z']+", '', n).lower()
		word_cache[word] = "#"


print(names_1)