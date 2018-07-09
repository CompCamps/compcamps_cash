import requests

class Prefix:
    def __init__(self, server):
        self.fetch()
        self.server = server

    def get(self):
        return self.prefix

    def fetch(self):
        req = requests.get(self.server + '/api/prefix')
        self.prefix = req.text.strip()