

"""
A first simple version of bank account
"""


def bank_account(initial_amount):
    balance = initial_amount
    while balance > 0:
        print ("Current balance: " + str(balance))
        cost = int(input("Input next payment:\n"))
        if cost <= balance:
            balance -= cost
        else:
            print ("Do not try to cheat!")
    print ("You are broke!")


"""
Test Driver
"""

bank_account(200.0);

