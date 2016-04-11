def subtractor(a, b): 
   """I subtract b from a and return the result"""  
   print("I'm a function. My name is {}".format(subtractor.__name__))
   print("I'm about to subtract {} and {}\n\n".format(a,b))
   return a - b  # i output a value by using the return statement


if __name__ == '__main__':
	subtractor(3, 2)
