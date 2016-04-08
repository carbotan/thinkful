for n in xrange(1, 101):
    print("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n)