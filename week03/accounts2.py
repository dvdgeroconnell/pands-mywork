# Weekly Task 03 - accounts.py

# Problem statement
# Reads in a 10 character account number and outputs the account number with only the last 4 digits
# showing (and the first 6 digits replaced by X's).

# Author(s): David O'Connell

print("Do you want to run the program for 10 digit fixed or for variable length account numbers")
choice = input("Enter F for Fixed, V for Variable, E to exit: ")

account = str(input("Enter a 10-digit account number: "))

length = len(account)

while length != 10:
    account_no = str(input("Please enter a valid 10-digit account number: "))
    length = len(account_no)

digits_to_hide = account_no[0:length-4]
new_account = account_no.replace(digits_to_hide, "XXXXXX")
print(f"Account number is: {new_account}")

# It is assumed that the account number can be no longer than the IBAN standard of 34 alphanumeric
# characters minus the first 4 which are 2 country code and 2 check digits - so 30 maximum.

account = str(input("Enter an account number: "))

length = len(account)
while length > 30:
    account_no = str(input("Please enter a valid account number: "))
    length = len(account_no)


digits_to_hide = account_no[0:length-4]
new_account = account_no.replace(digits_to_hide, "XXXXXX")
print(f"Account number is: {new_account}")