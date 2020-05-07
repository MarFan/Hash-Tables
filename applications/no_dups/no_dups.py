def no_dups(s):
    # Implement me.
    word_string = ""
    
    if len(s):
    	for w in s.split():
	    	if w not in word_string:
	    		if len(word_string):
	    			word_string += " "
	    		
	    		word_string += w

    return word_string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))