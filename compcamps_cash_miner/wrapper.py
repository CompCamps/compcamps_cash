import os

from compcamps_cash_api.entities import Block, Transaction, Keys, Prefix
from compcamps_cash_api.entities.block import nextBlock

import miner
import balance
import transaction

while(1):
    os.system('clear')
    print("Welcome to Campcoin miner")
    print("")
    print("Select an option:")
    print("(M) Start mining")
    print("(T) Send coins")
    print("(B) Check your balance or view your Public Key")
    print()
    print("Press Ctrl+C to exit")
    print()
    option = input("Enter a selection: ")

    if option == "B":
        balance.checkBalance()

    if option == "M":
        try:
            while True:
                miner.mine()
        except KeyboardInterrupt:
            pass
        

    if option == "T":
        transaction.sendCoins()