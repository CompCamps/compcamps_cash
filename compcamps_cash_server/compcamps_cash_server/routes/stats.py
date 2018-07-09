from flask import jsonify

from compcamps_cash_server import app
from compcamps_cash_server.routes import blocks

@app.route('/api/stats/blocksPerHour')
def getBlocksPerHour():
    blockchain = blocks.getBlockchain()
    stats = {}
    for block in blockchain:
        day = block.timestamp.strftime('%d')
        hour = block.timestamp.strftime('%H')
        try:
            stats[day][hour] = stats[day][hour] + 1
        except:
            try:
                stats[day][hour] = 1
            except:
                stats[day] = {}
                stats[day][hour] = 1
                
    return jsonify(stats)