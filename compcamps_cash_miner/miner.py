import hashlib

data = "hello world"

hash = hashlib.sha256(data.encode('utf-8')).hexdigest()

# TODO: Use a while loop here to change data and rehash until it starts with 0

if hash[0] != "0":
    print("Invalid Hash.")
else:
    print("Correct hash!")