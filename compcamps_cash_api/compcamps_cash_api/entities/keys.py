from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
import base64

class Keys:
    def __init__(self):
        self.public_key, self.private_key = self.loadKeys()

    def loadKeys(self):
        public_key = {}
        private_key = {}
        try:
            public_key = VerifyingKey.from_pem(open("public.pem").read())
            private_key = SigningKey.from_pem(open("private.pem").read())
            return public_key, private_key
        except:
            return self.generateKeys()

    def generateKeys(self):
        choice = input("No public/private key files found, generate now? (Y/N)")
        if choice == 'Y':
            # SECP256k1 is the Bitcoin elliptic curve
            private_key = SigningKey.generate(curve=SECP256k1) 
            public_key = private_key.get_verifying_key()

            file_out = open("private.pem", "wb")
            file_out.write(private_key.to_pem())

            file_out = open("public.pem", "wb")
            file_out.write(public_key.to_pem())

            return public_key, private_key
        else:
            exit()

    def getEncodedKeys(self):
        return str(base64.b64encode(self.public_key.to_string()), "utf-8"), str(base64.b64encode(self.private_key.to_string()), "utf-8")

    # sign data with a private key
    def signData(self, data):
        encoded = data.encode('utf8')
        signature = self.private_key.sign(encoded)
        return signature

# verifty message with public key and signature
def verifyData(data, public_key_string, signature):
    public_key = VerifyingKey.from_string(base64.b64decode(public_key_string), curve=SECP256k1)
    encoded = data.encode('utf8')
    try:
        public_key.verify(signature, encoded)
        return True
    except BadSignatureError:
        return False

