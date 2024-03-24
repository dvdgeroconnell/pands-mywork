# myFunctions.py

# Function to return the Fibonacci sequence of n entries where n is the number
# passed as the argument.

# Author(s): Andrew Beatty, David O'Connell

import logging
# Turn down the logging level for the moment...
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.CRITICAL)

def fibonacci(entries):
    fib = []
    m = 0
    n = 1
    if entries > 0:
        fib.append(m)
        if entries > 1:
            fib.append(n)
            if entries > 2:
                count = 2
                while count < entries:
                    p = m + n
                    fib.append(p)
                    m,n = n,p
                    count += 1
    if entries < 0:                
        raise ValueError("Number must be > 0")
    else:
        logging.debug("%d: %s", entries, fib)

    return fib

if __name__ == '__main__':
    # tests go here
    print("running this module as main")

    return7 = [0, 1, 1, 2, 3, 5, 8]
    return11 =[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    #These actually run the code
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return for 0'
    assert fibonacci(1) == [0], 'incorrect return for 1'

    try:
        fibonacci(-1)
    except ValueError:
        # We want this exception to be thrown so do nothing to intercept it here
        # print("Got ValueError")
        pass
    else:
        # If the exception was not thrown, we should throw an AssertionError
        assert False, "fibonacci missing ValueError"
        