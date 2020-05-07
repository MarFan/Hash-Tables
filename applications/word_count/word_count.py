import re

def word_count(s):
    # Implement me.

    word_cache = {}

    for w in s.split():
    	if len(w) is None:
    		return	
    	
    	word = re.sub('[^A-Za-z\']+', '', w).lower()
    	
    	if word not in word_cache:
    		word_cache[word] = 1
    	else:
    		word_cache[word] += 1
    
    return word_cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))