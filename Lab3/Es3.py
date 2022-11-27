import json
import numpy as np
import requests


class DeviceManager():
    def __init__(self, url, inputDictionary):
        self.url = url
        self.inputDictionary = inputDictionary
        r = requests.get(self.url+"/get-stations")
        self.dictionary = r.json()
        self.numberStat = len(self.dictionary["stations"])
        self.menu()

    def slots(self, _N = 10, _order = -1):
        list = []
        newDict = self.dictionary
        for i in range(self.numberStat):
            list.append(self.dictionary["stations"][i]["slots"])
        index = np.argsort(list)[::_order]
        for i in range(_N):
            newDict["stations"][i] = self.dictionary["stations"][index[i]]
        
        return json.dumps(newDict["stations"][:_N], indent=4)

    def bikes(self):
        pass
        #return json.dumps(output, indent=4)

    def electrical(self):
        pass
        #return json.dumps(output, indent=4)

    def count(self):
        pass
        #return json.dumps(output, indent=4)

    def out(self):
        return self.output

    def menu(self):
        command = self.inputDictionary["command"]
        if command == "order_slots":
            self.output = self.slots()
        elif command == "order_bikes":
            self.output = self.bikes()
        elif command == "electrical_bikes":
            self.output = self.electrical()
        elif command == "count":
            self.output = self.count()
        elif command == "quit":
            pass
