from flask import jsonify, request, send_file
import simplejson as json

# Imports for Image manip
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os, io

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

def drawBalance(balance):
    img = Image.open(os.path.abspath("./compcamps_cash_server/routes/assets/template.png"))
    img_io = io.BytesIO()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.abspath("./compcamps_cash_server/routes/assets/SourceSansPro-Regular.otf"), 200)
    bLength = len(str(int(balance)))
    draw.text((550-bLength*55, 50),str(int(balance)),(255,255,255),font=font)
    img.save(img_io, 'png', quality=100)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

@app.route('/api/balance')
def balance():
    key = request.args.get('public_key')
    image = request.args.get('image')
    balance = getBalance(key)
    if not image:
        return str(balance)
    else:
        return drawBalance(balance)

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