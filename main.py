import datetime  # import date module


# help('FORMATTING')

# Dummy Data Dictionary
# TODO: Create an "Account-Holders" Dictionary
# TODO: Place User dictionaries inside Account-Holders dictionary
# These dictionaries will be used to Create_Read_Update_Delete -CRUD- User's data on each view.

# User Class not in use yet.
# We will be using this class to CREATE user accounts and add them to our Dictionary of Users.
class User:
    # Initializing & assigning the given parameters to class attributes.
    def __init__(self, pin, first, last, dob, cash, age, debit, saving, credit, credit_used, address,
                 debit_transactions, savings_transactions, credit_transactions):
        self.pin = pin
        self.first = first
        self.last = last
        self.dob = dob
        self.cash = cash
        self.age = age
        self.debit = debit
        self.saving = saving
        self.credit = credit
        self.credit_used = credit_used
        self.address = address
        self.debit_transactions = debit_transactions
        self.savings_transactions = savings_transactions
        self.credit_transactions = credit_transactions


# Reference to dummy user account that lacks parent dictionary.
user_1 = {
    'pin': 0000,
    'first': 'Matulu',
    'last': 'Shakur',
    'dob': '00/00/00',
    'cash': 1386,
    'debit': 3218,
    'saving': 247,
    'credit': 900,
    'credit_used': 113,
    'address': '1884 ECU Blvd.',
    'state': '1884 ECU Blvd.',
    'debit_transactions': [],
    'savings_transactions': [],
    'credit_transactions': []
}

# Today's Date using function from 'datetime' module
date = str(datetime.date.today())

# Display user-name & date
print(f"\n\n{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
# Display Divider
print('-' * 35)

# USER COMMAND LINE
print(f'{"0 : Checking":20} {"1 : Credit":16s}')
print(f'{"2 : Saving":20s} {"3 : Profile":16s}')
print(f'{"4 : Exit":20s}\n')

# Prompt User for Command-Line selection.
user_input = input('Enter your selection:\n').strip().lower()
# Add whitespace to separate views/screens/pages
print('\n\n\n\n\n')

# If the User input = EXIT, end program.
if user_input.lower() != 'exit':
    if user_input == '0' or user_input.lower() == 'checking':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        # Display 'CHECKING' COMMAND-LINE OPTIONS
        print(f'{"Balance":<7} :   $ {user_1["debit"]:<10}')
        print(f'{"0 : Transactions":20s} {"1 : Deposit":16s}')
        print(f'{"2 : Withdraw":20s} {"3 : Exit":16s}\n')

        # PROMPT USER FOR 2ND COMMAND
        user_input = input('Enter your selection:\n')

    if user_input == '1' or user_input.lower() == 'deposit':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        # Display 'DEPOSIT' COMMAND-LINE OPTIONS
        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')

        # PROMPT USER FOR 2ND COMMAND
        user_input = input('Enter your selection:\n')

    if user_input == '2' or user_input.lower() == 'saving':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        # Display 'SAVING' COMMAND-LINE OPTIONS
        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

    if user_input == '3' or user_input.lower() == 'credit':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        # Display 'CREDIT' COMMAND-LINE OPTIONS
        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

    if user_input == '4' or user_input.lower() == 'profile':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        # Display 'CREDIT' COMMAND-LINE OPTIONS
        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

    if user_input == '5' or user_input.lower() == 'exit':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        # Display 'CREDIT' COMMAND-LINE OPTIONS
        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

print('\n\nThank you for using XYZ Bank. Have a great day!')
"""
print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
print(f'{"2 : Make Withdraw":20s} {"3 : Option 4":16s}')
print(f'{"4 : Edit Profile":20s} {"5 : Exit":16s}')
"""
