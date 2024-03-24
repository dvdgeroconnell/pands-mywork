# a module of useful functions
# Author: Andrew Beatty
import logging
logging.basicConfig(filename="./bank.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d")

balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        logging.critical(f"the amount ({amount}) should never be less than 0")
        raise ValueError("amount should always be greater than 0")
    if amount > balance:
        logging.critical(f"trying to withdraw more ({amount}) than is in account ({balance})")
        raise ValueError("not enough funds")
    balance = balance - amount
    logging.info(f"we have just withdrawn {amount} new balance is{balance}")
    return balance

if __name__ == "__main__":
    assert withdraw(20) == 80 , "incorrect calculation"
    try:
        print("Testing1")
        x = withdraw(-1)
        print("x is ", x)
        assert False, "should have thrown a value error"
    except ValueError as ve:
        print("here1")
        pass
    
    try:
        withdraw(110)
        assert False, "can't withdraw more than is in balance"
    except ValueError as ve:
        print("here2")
        pass
    print ("all good")
    