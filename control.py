from bank import *
import os.path

newOrExisting = input('To create a new account, Enter: new. To access account, Enter: existing\n Enter: ')

if newOrExisting == 'new':
    username = input('Please enter username: ')
    user = Account(username)
    password = input('Please create a password: ')
    user.createAccount(password)
    print('Account Created! Restart program and enter as an existing account.')

if newOrExisting == 'existing':
    username = input('Please enter username: ')
    if os.path.exists(f"C:\\Users\\krist\\.vscode\\Python_Files\\{username}.txt") == True:
        user = Account(username)
        password = input('Please enter password: ')
        user.checkBoth(password, username)

        if user.incorrect == True:
            print('Incorrect Password. Please restart')
            
        elif user.incorrect == False:
            choice = input('To withdraw, enter: withdraw. To deposit, enter: deposit. To check balance, enter: balance.\n Enter:')
            
            if choice == 'withdraw':
                amount = int(input('Enter amount to withdraw: '))
                user.withdraw(amount, username)
            
            elif choice == 'deposit':
                depmoney = input('Enter amount to deposit: ')
                user.deposit(depmoney, username)

            elif choice == 'balance':
                user.checkbalance(username)

    else:
        print('Username does not exist or already taken, try again')