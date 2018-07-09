from .keys import verifyData
import base64

class Transaction:
    def __init__(self, sender, reciever, amount, signature=None, timestamp=None):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.timestamp = timestamp
        if signature:
            self.signature = signature

    def sign(self, keys):
        self.signature = base64.b64encode(keys.signData(str(self.sender) + str(self.reciever) + str(self.amount)))

    def verify(self, public_key_string):
        return verifyData(str(self.sender) + str(self.reciever) + str(self.amount),
                    public_key_string,
                    base64.b64decode(self.signature))

    def _asdict(self):
        return self.__dict__
