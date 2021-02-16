from Block import *
from Transaction import *

class Node:
    def __init__(self, genesisBlock: Block = None, nodeID = None):
        self.id = nodeID

    def verifyTranscation(self, tx : Transaction):
        return None

    def writeToFile():
        return None