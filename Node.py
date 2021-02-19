from Block import *
from Transaction import *
from typing import List
from hashlib import sha256

class Node:
    def __init__(self, genesisBlock: Block = None, nodeID = None):
        self.id = nodeID
        self.blockChain = BlockChain(genesisBlock)
        self.globalUnverifiedTxPool : List[Transaction] = []
        self.miningDifficulty = 0x07FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    
    def miningBlock(self, tx : Transaction):
        if self.verifyTranscation(tx):
            nonce = 0
            blockPOW = str(self.miningDifficulty + 1)
            #TODO: Check if prev is the pow
            prevBlockNode = self.blockChain.last_block
            prevHashing = prevBlockNode.curBlock.hashing()
            txAndPrevBeforeHash = tx.toString() + prevHashing
            while int(blockPOW, 16) > self.miningDifficulty:
                blockInfo = txAndPrevBeforeHash + str(nonce)
                blockPOW = sha256(blockInfo.encode('utf-8')).hexdigest()
                nonce += 1
            nonce -= 1

            #TODO: add to the longest chain
            newBlock = Block(tx, prevHashing, nonce, blockPOW)
            newBlockLinkedNode = BlockLinkedNode(prevBlockNode, newBlock, prevBlockNode.height + 1)
            self.broadCastBlock(newBlock)
            self.addBlockToChain(newBlockLinkedNode)

    def verifyTranscation(self, tx : Transaction):
        return None

    def broadCastBlock(self):
        return None
    
    def addBlockToChain(newBlockLinkedNode : blockLinkedNode):
        self.blockChain.addBlock(newBlockLinkedNode)

    def writeToFile():
        return None