from flask import jsonify, request
import simplejson as json

from compcamps_cash_api.entities import Block, Transaction
from compcamps_cash_server import app, db, utils, prefix
from compcamps_cash_server.routes import transactions

def getBlockchain(limit=0, sortOrder=-1):
    blockchain = []
    blocks = db.blocks.find().sort([('$natural', sortOrder)]).limit(limit)
    for block in blocks:
        b = Block(block['index'], block['transactions'], block['nonce'], block['previousHash'], utils.utcToRegina(block['_id'].generation_time))
        blockchain.append(b)
    return blockchain

@app.route('/api/blocks')
def getBlocks():
    limit = request.args.get('limit') or 0
    return jsonify(getBlockchain(int(limit), 1))

@app.route("/api/blocks", methods=["POST"])
def mineBlock():
    previousBlock = getBlockchain(1)[0]
    transactionList = transactions.findTransactions()

    req = request.get_json()
    block = Block(req["index"], req["transactions"], req["nonce"], previousBlock.hash)
   
    if not block.validate(prefix):
        return jsonify({"error": "Invalid hash"}), 400

    for transaction in json.loads(block.transactions):
        transactionObject = Transaction(transaction["sender"], transaction["reciever"], transaction["amount"], transaction["signature"])

        if not transaction["sender"] == "MINER":
            if not transactionObject.verify(transactionObject.sender):
                return jsonify({"error": "Bad signature in transaction"}), 400

            for trans in transactionList:
                if trans.signature == transactionObject.signature:
                    db.transactions.delete_one({"signature": transactionObject.signature })
                    transactionList.remove(trans)
                    break
            else:
                return jsonify({"error": "Attempting to mine a non-existent transaction"}), 400

        elif transactionObject.amount != 1:
                return jsonify({"error": "Transaction mining reward must be 1"}), 400
    
    insertBlock = Block(block.index, block.transactions, block.nonce, block.previousHash, block.hash)
    db.blocks.insert_one(insertBlock.__dict__)

    return jsonify({"message": "New block successfully mined!"}), 200

@app.route("/api/blocks/latest")
def getLatestBlock():
    latest = getBlockchain(1)[0]
    return jsonify(latest)