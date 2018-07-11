from compcamps_cash_api.entities import Block, Transaction, Prefix, Keys
from compcamps_cash_api import CompCampsCashApi

ccapi = CompCampsCashApi("https://compcamps-cash.herokuapp.com")

prefix = ccapi.getPrefix()
# Calls the keys class from the ccapi
myKeys = Keys()
public_key, _ = myKeys.getEncodedKeys()

transactions = ccapi.getPendingTransactions() # Gets the current transactions from the server

# TODO: Replace your key string with the variable public_key
transaction = Transaction("MINER", "PTPfVMu//rJr9SEeBXdr45cB/cdLYeoj6eMt93PqzkhzjUZz/4Et/o6xy0jg7WvdOvxEB78J81QG3VM0htWyzw==", 1)

#TODO: Sign your transaction with your keys

nonce = 0
previousBlock = ccapi.getCurrentBlock()

block = Block(previousBlock.index + 1, transactions, nonce, previousBlock.hash)

while not block.validate(prefix):
    nonce = nonce + 1
    block = Block(previousBlock.index + 1, transactions, nonce, previousBlock.hash)

res = ccapi.postBlock(block)
print(res)

if not block.validate(prefix):
    print("Invalid Hash.")
else:
    print("Correct hash!")