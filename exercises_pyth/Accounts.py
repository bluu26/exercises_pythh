from Account_class import Account
accounts = []
menu = """
1 - show all
2 - add account
3 - deposit
4 - withdraw
5 - exit
"""


while True:
    user_input = input(menu)
    if user_input == "1":
        print("konta w systemie: ")
        for account in accounts:
            print(account.numer, account.stan)
    elif user_input == "2":
        number = input("Enter account number: ")
        k = Account(number, 0)
        accounts.append(k)
    if user_input == "5":
        break
