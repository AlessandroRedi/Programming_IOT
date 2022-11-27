import json
import numpy as np
import requests


class DeviceManager():
    def __init__(self):
        self.dictionary = json.load(open("C:\\Users\\aledi\\Desktop\\Alessandro\\PoliTo\\Magistrale\\Programming_IOT\\lab4\\Sensor.json"))

    def temperature(self):

        return json.dumps(self.dictionary)

    def humidity(self):
        
        return json.dumps(self.dictionary)

    def both(self):
        
        return json.dumps(self.dictionary)