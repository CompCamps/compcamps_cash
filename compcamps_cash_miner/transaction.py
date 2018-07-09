import os
from init import ccapi, public_key, myKeys
from compcamps_cash_api import Transaction

def sendCoins():
    os.system('clear')
    reciever = input("Enter address to send coins to: ")
    amount = input("Enter amount to send: ")
    transaction = Transaction(public_key, reciever, float(amount))
    transaction.sign(myKeys)
    ccapi.postTransaction(transaction)
    
    input("Press any key to return to menu...")