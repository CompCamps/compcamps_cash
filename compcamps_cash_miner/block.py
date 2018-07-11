import hashlib

class Block:
    def __init__(self, index, data, nonce, previousHash):
        self.index = index
        self.data = data
        self.nonce = nonce
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        toHash = str(self.index) + self.data +  #include nonce!
        
        return # Move the hashing code to this function
    
    def validate(self):
        return self.hash[0] == "0"