from typing import List

class TxOutput:
    def __init__(self, value = None, pubkey = None, outputJsonObj = None):
        if outputJsonObj:
            self.__getWithJson(outputJsonObj)
            return
        self.value = value
        self.pubkey = pubkey

    def __getWithJson(self, jsonObj):
        self.value = int(jsonObj['value'])
        self.pubkey = jsonObj['pubkey'].encode('utf-8')

class TxInput:
    def __init__(self, number = None, output : TxOutput = None, inputJsonObj = None):
        if inputJsonObj:
            self.__getWithJson(inputJsonObj)
            return
        self.number = number
        self.output = TxOutput(output.value, output.pubkey)


    def __getWithJson(self, jsonObj):
        self.number = jsonObj['number']
        self.output = TxOutput(outputJsonObj=jsonObj['output'])


class Transaction:
    def __init__(self, txNumber = None, inputList : List[TxInput] = None, outputList : List[TxOutput] = None, sig = None, jsonObj = None):
        if jsonObj:
            self.__getTxWithJson(jsonObj)
            return
        self.txNumber = txNumber
        self.inputList = inputList
        self.outputList = outputList
        self.sig = sig

    def __getTxWithJson(self, jsonObj):
        jsonObj = jsonObj
        self.txNumber = jsonObj['number']
        self.inputList = []
        self.outputList = []
        self.sig = jsonObj['sig']

        for txInput in jsonObj['input']:
            self.inputList.append(TxInput(inputJsonObj=txInput))

        for txOutput in jsonObj['output']:
            self.outputList.append(TxOutput(outputJsonObj=txOutput))





