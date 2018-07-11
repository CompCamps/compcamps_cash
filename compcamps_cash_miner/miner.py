from compcamp_cash_api.entities import Block
from compcamps_cash_api import CompCampsCashApi

ccapi = CompCampsCashApi("https://compcamps-cash.herokuapp.com")

data = "hello world"
nonce = 0
# TODO: Instead of a blank block, use the ccapi to getCurrentBlock() from the server
previousBlock = 

# TODO: create the next block using the previousBlock values
block = 

# TODO: Change our loop to use our block's validate function
while not block.validate("0"):
    nonce = nonce + 1
    block = # This line should match line 13

if block.hash[0] != "0":
    print("Invalid Hash.")
else:
    print("Correct hash!")