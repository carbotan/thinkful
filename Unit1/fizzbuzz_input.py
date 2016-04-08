n = 1

while True:
    try:
        num = int(input("Welcome to FizzBuzz!  Enter a positive number."))
        if num < 1:
            raise ValueError()
        break
    except ValueError:
        print("That was not a number.")
    except DivideByZeroError:
        print("NOPE")


#while num < 1:
#    num = float(input("Enter a positive number."))
#    continue
    
while n > 0 and n < num:
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else: 
        print(n)
    n += 1
