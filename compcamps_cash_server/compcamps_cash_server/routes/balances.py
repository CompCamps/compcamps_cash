from flask import jsonify, request
import simplejson as json

from compcamps_cash_api.entities import Block
from compcamps_cash_server import app
from compcamps_cash_server.routes import blocks

def getBalance(public_key):
    balance = 0
    blockchain = blocks.getBlockchain()
    for block in blockchain:
        for transaction in json.loads(block.transactions):
            if (transaction["reciever"] == public_key):
                balance = balance + transaction["amount"]
            if (transaction["sender"] == public_key):
                balance = balance - transaction["amount"]

    return balance

def hasSufficentFunds(public_key, amount):
    balance = getBalance(public_key)
    return balance >= amount

@app.route('/api/balance')
def balance():
    key = request.args.get('public_key')
    image = request.args.get('image')
    balance = getBalance(key)
    return str(balance)

@app.route('/api/balances')
def getAllBalances():
    balances = {}
    blockchain = blocks.getBlockchain()
    for block in blockchain:
        for transaction in json.loads(block.transactions):
            try:
                balances[transaction["reciever"]] = balances[transaction["reciever"]] + transaction["amount"]
            except:
                balances[transaction["reciever"]] = transaction["amount"]

            try:
                balances[transaction["sender"]] = balances[transaction["sender"]] - transaction["amount"]
            except:
                balances[transaction["sender"]] = 0 - transaction["amount"]

    del balances["MINER"]
    return jsonify(balances)