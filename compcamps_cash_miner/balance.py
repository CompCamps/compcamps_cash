import os
from init import ccapi, public_key

def checkBalance():
    balance = ccapi.getBalance(public_key)
    os.system('clear')
    print("Your public key is: " + public_key)
    print("Your balance is: " + balance)
    print("")
    input("Press any key to return to menu...")