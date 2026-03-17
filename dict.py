

def build_dict(filename):
    """ takes the name of a text file and builds a dictionary 
        in which each key is a lower-case letter and the corresponding 
        value is a list of all words from the file that begin with 
        that letter
    """
    # read in the file as one big string    
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    # split the file into a list of words
    words = text.split()
    
    # start with an empty dictionary
    d = {}
    
    for w in words:
        w = w.lower()
        # add code that updates the dictionary to include word w
        if w[0] not in d:
            d[w[0]] = [w]
            
        else:
            d[w[0]] += [w]
            
    return d
        