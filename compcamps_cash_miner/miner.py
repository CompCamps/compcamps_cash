import hashlib
from block import Block

data = "hello world"
nonce = 0
# Creates a genesis block
block = Block(0, data, nonce, 0)

# TODO: Move this into the Block class
hash = hashlib.sha256(data.encode('utf-8')).hexdigest()

# TODO: Change our loop to use our block's validate function
while hash[0] != "0":
    nonce = nonce + 1
    block = Block(0, data, nonce, 0)

if block.hash[0] != "0":
    print("Invalid Hash.")
else:
    print("Correct hash!")