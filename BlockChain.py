import json
import logging
from typing import List
from hashlib import sha256 as H
from Transaction import *
from Block import *


logging.basicConfig(filename='main.log', filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("my-logger")
logger.handlers = []

class BlockChain:
    def __init__(self, genesisBlock : Block = None):
        """
        Constructor for the `Blockchain` class.
        """
        logger.info("Initilizing BlockChain....")
        self.chain : List[Block] = None
        self.chain.append(genesisBlock)
        logger.info('Initilizing done!')

    @staticmethod
    def createGenesisBlock(self):
        genesisTx = self.__getGenesisTx(self)
        genesisPrev = H(b'genesis prev').hexdigest()
        genesisNonce = 0
        genesisPOW = H(b'genesis POW').hexdigest()

        genesisBlock = Block(genesisTx, genesisPrev, genesisNonce, genesisPOW)
        
        # self.chain.append(self.genesisBlock)
        logger.info('Genesis Block has been created successfully!')
        return genesisBlock
    
    def __getGenesisTx(self):
        with open("./transactions/genesisTx.json") as f:
            jsonObj = json.load(f)
        genesisTx = Transaction(jsonObj=jsonObj[0])

        return genesisTx

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification (proof is valid and 
        previous_hash match with the hash of last block).
        """
        # if block.prev != self.last_block.
        return None



