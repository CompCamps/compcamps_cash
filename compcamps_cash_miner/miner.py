import hashlib
from block import Block

data = "hello world"
nonce = 0
# Creates a genesis block
block = Block(0, data, nonce, 0)

# TODO: Move this into the Block class
hash = hashlib.sha256(data.encode('utf-8')).hexdigest()

# TODO: Use a while loop here to change data and rehash until it starts with 0
while not block.validate():
    nonce = nonce + 1
    block = Block(0, data, nonce, 0)

if block.hash[0] != "0":
    print("Invalid Hash.")
else:
    print("Correct hash!")