import json
from hashlib import sha256 as H
from Transaction import *
from Block import Block
import logging

logging.basicConfig(filename='main.log', filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("my-logger")
logger.handlers = []

class MVB:
    def __init__(self):
        """
        Constructor for the `Blockchain` class.
        """
        logger.info("Initilizing MVB....")
        self.chain = []
        self.__createGenesisBlock()
        logger.info('Initilizing done!')

    def __createGenesisBlock(self):
        genesisTx = self.__getGenesisTx()
        genesisPrev = H(b'genesis prev').hexdigest()
        genesisNonce = 0
        genesisPOW = H(b'genesis POW').hexdigest()

        self.genesisBlock = Block(genesisTx, genesisPrev, genesisNonce, genesisPOW)
        logger.info('Genesis Block has been created successfully!')
        

    def __getGenesisTx(self):
        with open("./transactions/genesisTx.json") as f:
            jsonObj = json.load(f)
        genesisTx = Transaction(jsonObj=jsonObj[0])
        return genesisTx