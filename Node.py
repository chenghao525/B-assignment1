from Block import *
from Transaction import *
from hashlib import sha256

class Node:
    def __init__(self, genesisBlock: Block = None, nodeID = None):
        self.id = nodeID
        self.blockChain = BlockChain(genesisBlock)
        self.miningDifficulty = 0x07FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    
    def miningBlock(self, tx : Transaction):
        if self.verifyTranscation(tx):

            nonce = 0
            blockPOW = str(self.miningDifficulty + 1)
            #TODO: Check if prev is the pow
            prev = self.blockChain[-1].proofOfWork
            txAndPrevBeforeHash = tx.toString() + prev
            while int(blockPOW, 16) > self.miningDifficulty:
                blockInfo = txAndPrevBeforeHash + str(nonce)
                blockPOW = sha256(blockMessage.encode('utf-8')).hexdigest()
                nonce += 1
            nonce -= 1

            #TODO: add to the longest chain
            newBlock = Block(tx, prev, nonce, blockPOW)
            self.broadCastBlock(newBlock)
            

    def verifyTranscation(self, tx : Transaction):
        return None

    def broadCastBlock(self):
        return None

    def writeToFile():
        return None