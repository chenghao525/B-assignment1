from Block import Block
from BlockChain import BlockChain
from Node import *
from Transaction import *
from threading import Thread
import random
from time import *
import json


class Driver:

    def __init__(self):
        self.nodeList = []
        self.globalUnverifiedTxPool : Transaction = []
        myMVB = BlockChain()
        # create genesis Block via static method
        self.genesisBlock = BlockChain.createGenesisBlock(BlockChain)
        self.__startNodesThread(8)
        self.__readTxFromFile()
        # print(self.nodeList)

    def __startNodesThread(self, count):
        for id in range(1, count + 1):
            node = Node(self.genesisBlock, id)
            self.nodeList.append(node)
            nodeThread = Thread(target=self.nodeMining, args=(node,))
            nodeThread.start()

    # TODO: implement node minig functionality
    def nodeMining(self, node):
        while True:
            #TODO: how to check if no more tx
            if len(self.globalUnverifiedTxPool) == 0:
                sleep(1)
                if len(self.globalUnverifiedTxPool) == 0:
                    break
            for tx in self.globalUnverifiedTxPool:
                node.miningBlock(tx)
                self.globalUnverifiedTxPool.remove(tx)
        node.writeToFile()
            
    
    # TODO: make the file name modifiable
    def __readTxFromFile(self):
        with open("./transactions/doubleSpendTx.json") as f:
            jsonObj = json.load(f)
        for obj in jsonObj['txList']:
            sleep(random.uniform(0, 1))
            self.globalUnverifiedTxPool.append(Transaction(jsonObj=obj))

if __name__ == "__main__":
    testDriver = Driver()