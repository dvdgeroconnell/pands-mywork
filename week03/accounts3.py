# Weekly Task 03 - accounts.py

# Problem statement
# Reads in a 10 character account number and outputs the account number with only the last 4 digits
# showing (and the first 6 digits replaced by X's).
# Extend the program to deal with account numbers of any length - state assumptions.

# Author(s): David O'Connell

# Ask the user if it is a 10 digit fixed or a variable length account number.
# Variable length will also work with 10 digits.
print("Do you want to run the program for 10 digit fixed or for variable length account numbers")
choice = input("Enter F for Fixed, V for Variable, anything else to exit: ")
proceed = False

if choice == 'F':
    account_no = str(input("Enter a 10-digit account number: "))

    while len(account_no) != 10:
        account_no = str(input("Please enter a valid 10-digit account number: "))

    #digits_to_hide = account_no[0:length-4]
    #hidden_account = account_no.replace(digits_to_hide, "XXXXXX")
    #print(f"Account number is: {hidden_account}")
    proceed = True

elif choice == 'V':

    # It is assumed that an account number can be no longer than the IBAN standard of 34 alphanumeric
    # characters minus the first 4 which are 2 country code and 2 check digits - so 30 maximum.

    account_no = str(input("Enter an account number: "))
    while len(account_no) > 30:
        account_no = str(input("Please enter a valid account number: "))
    proceed = True

if proceed:
    length = len(account_no)
    count = 0
    hidden_account = account_no
    replace_string = ''
    while count < (length - 4):
        replace_string = replace_string + "X"
        count += 1

#create the original and replacement strings as required by the replace function
    digits_to_hide = hidden_account[0:length-4]
    hidden_account = hidden_account.replace(digits_to_hide, replace_string)
    print(f"Account number is: {hidden_account}")
else:
    print("Exiting")