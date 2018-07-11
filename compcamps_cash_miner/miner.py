from compcamps_cash_api.entities import Block, Transaction, Prefix
from compcamps_cash_api import CompCampsCashApi

ccapi = CompCampsCashApi("https://compcamps-cash.herokuapp.com")

prefix = ccapi.getPrefix()

transactions = ccapi.getPendingTransactions() # Gets the current transactions from the server
# TODO: create a new transaction
# TODO: Add your transaction to the transactions array

nonce = 0
previousBlock = ccapi.getCurrentBlock()

block = Block(previousBlock.index + 1, transactions, nonce, previousBlock.hash)

while not block.validate(prefix):
    nonce = nonce + 1
    block = Block(previousBlock.index + 1, transactions, nonce, previousBlock.hash)

if block.hash[0] != "0":
    print("Invalid Hash.")
else:
    print("Correct hash!")