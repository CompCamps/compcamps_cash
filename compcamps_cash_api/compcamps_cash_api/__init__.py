from .entities import Block
from .entities import Transaction

import requests
import urllib
import simplejson as json

class CompCampsCashApi:
    def __init__(self, server):
        self.server = server

    def getCurrentBlock(self):
        req = requests.get(self.server + '/api/blocks/latest')
        if req.status_code == 200:
            res = req.json()
            return Block(res['index'], res['transactions'], res['nonce'], res['previousHash'], res['timestamp'])
        else:
            return req

    def postBlock(self, block):
        req = requests.post(self.server + '/api/blocks', json=block)
        if req.status_code == 200:
            return True
        else:
            print(req.json()["error"])
            return False

    def getPendingTransactions(self):
        req = requests.get(self.server + '/api/transactions/pending')
        transactions = []
        for trans in req.json():
            transactions.append(Transaction(trans['sender'], trans['reciever'], trans['amount'], trans['signature']))
        return transactions
    
    def postTransaction(self, transaction):
        req = requests.post(self.server + '/api/transactions', json=transaction)
        if req.status_code == 200:
            return True
        else:
            print(req.json()["error"])
            return False

    def getBalance(self, public_key):
        key = {'public_key': public_key}
        req = requests.get(self.server + '/api/balance?' + urllib.parse.urlencode(key))
        if req.status_code == 200:
            return req.text
        else:
            return False

    def getPrefix(self):
        req = requests.get(self.server + '/api/prefix')
        if req.status_code == 200:
            return req.text
        else:
            return False
        