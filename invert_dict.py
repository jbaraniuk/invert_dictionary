#Justin Baraniuk 
#February 25, 2021

def invert_dict(d):
	 """Creates a dictionary that maps from frequencies to letters.
    d: dict
    returns: dict
    """
	
    inverse = {}
    for key in d:
        value = d[key]
        inverse.setdefault(value,[]).append(key)
    return inverse