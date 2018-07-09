import datetime as date

from compcamps_cash_api.entities import Block, Transaction, Keys, Prefix
from compcamps_cash_api.entities.block import nextBlock
from compcamps_cash_api import CompCampsCashApi

from init import myKeys, public_key, ccapi

def getLatestBlock():
    return ccapi.getCurrentBlock()

def getLatestTransactions():
    #Get transactions waiting to be mined
    transactions = ccapi.getPendingTransactions()

    # Add a transaction paying yourself a coin
    transaction = Transaction("MINER", public_key, 1)
    transaction.sign(myKeys) # Sign the transaction with your keys
    transactions.append(transaction)

    return transactions

def mine():
    # Get latest block & transactions to mine
    previousBlock = getLatestBlock()
    transactions = getLatestTransactions()
    prefix = ccapi.getPrefix()

    # Some debug info
    print("Current prefix: " + prefix)
    print("Currently mining block: ")
    previousBlock.display()
    
    # Mine the block by incrementing the nonce
    nonce = 0
    block = nextBlock(previousBlock, transactions, nonce)
    beginTimestamp = date.datetime.now()
    while not block.validate(prefix):
        nonce = nonce + 1
        block = nextBlock(previousBlock, transactions, nonce)

        # Check the server every 5 seconds incase someone else mined before us
        if ((date.datetime.now() - beginTimestamp).total_seconds() > 5):
            beginTimestamp = date.datetime.now()
            previousBlock = getLatestBlock()
            transactions = getLatestTransactions()
            prefix = ccapi.getPrefix()

    res = ccapi.postBlock(block) # Submit the block to the server
    if res:
        print("Block successfully mined!")