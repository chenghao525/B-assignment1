import hashlib

class Block:
    def __init__(self,tx = None, prev = None, nonce = None, proofOfWork = None):
        self.tx = tx
        self.prev = prev
        self.nonce = nonce
        self.proofOfWork = proofOfWork

    
    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.tx).encode('utf-8'))
        key.update(str(self.prev).encode('utf-8'))
        key.update(str(self.nonce).encode('utf-8'))
        return key.hexdigest()
 