from flask import jsonify, request
import simplejson as json

from compcamps_cash_api.entities import Transaction
from compcamps_cash_server import app, db, utils
from compcamps_cash_server.routes import balances, blocks

def findTransactions(limit=0):
    transactions = []
    for transaction in db.transactions.find().sort([('$natural', 1)]).limit(limit):
        t = Transaction(transaction['sender'], transaction['reciever'], transaction['amount'], transaction['signature'], utils.utcToRegina(transaction['_id'].generation_time))
        transactions.append(t)
    return transactions
    
@app.route("/api/transactions/pending")
def getPendingTransactions():
    limit = request.args.get('limit') or 0
    transactions = findTransactions(int(limit))
    return jsonify(transactions)

@app.route('/api/transactions/mined')
def getMinedTransactions():
    transactions = []
    blockchain = blocks.getBlockchain()
    for block in blockchain:
        for transaction in json.loads(block.transactions):
            if (transaction['sender'] != "MINER"):
                trans = Transaction(transaction['sender'], transaction['reciever'], transaction['amount'], transaction['signature'], block.timestamp)
                transactions.append(trans)

    return jsonify(transactions)

@app.route("/api/transactions", methods=['POST'])
def createTransaction():
    req = request.get_json()
    transactionObject = Transaction(req["sender"], req["reciever"], req["amount"], req["signature"])

    if not transactionObject.verify(transactionObject.sender):
        return jsonify({"error": "Invalid signature"}), 400

    if not balances.hasSufficentFunds(transactionObject.sender, transactionObject.amount):
        return jsonify({"error": "Insufficient Balance"}), 400
    
    if transactionObject.sender == transactionObject.reciever:
        return jsonify({"error": "You cannot send yourself coins!"}), 400

    if transactionObject.amount <= 0:
        return jsonify({"error": "Must send at least 1 coin"}), 400

    if (len(str(transactionObject.__dict__)) > 500):
        return jsonify({"error": "Transaction Object exceeds maximum bytes"}), 400 

    db.transactions.insert_one(transactionObject.__dict__)
    return jsonify({"response": "Transaction Posted"})