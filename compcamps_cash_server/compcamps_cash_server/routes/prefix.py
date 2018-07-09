from compcamps_cash_server import app, prefix

@app.route("/api/prefix")
def getPrefix():
    return prefix