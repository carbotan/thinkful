def mattmath(a, b, c):
    """I add a, b, and c and return the result"""
    print("My name is {}.  I am testing functcions.".format(mattmath.__name__))
    print("I am about to add {} and {} and {}\n\n".format(a,b,c))
    return a + b + c
    
if __name__ == '__main__':
	mattmath(1, 2, 3)