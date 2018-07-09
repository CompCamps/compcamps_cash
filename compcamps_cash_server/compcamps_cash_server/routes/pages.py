from flask import render_template, send_from_directory, send_file

from compcamps_cash_server import app

@app.route('/')
def indexRoute():
    return render_template("index.html")

@app.route('/stats')
def statsRoute():
    return render_template("stats.html")
    
@app.route('/transactions')
def transactionsRoute():
    return render_template("transactions.html")

@app.route('/balance')
def balanceRoute():
    return render_template("balance.html")

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('views', path)