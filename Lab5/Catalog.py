import numpy as np
import json
import cherrypy
import requests

class GreenHouseCatalog():
    exposed = True

    def __init__(self):
        self.DictCatalog = json.load(open("C:\\Users\\aledi\\Desktop\\Alessandro\\PoliTo\\Magistrale\\Programming_IOT\\lab5\\catalog.json"))

    def GET(self, *uri, **query):
        out = []
        if uri[0] == "broker":
            out.append(self.DictCatalog[uri[0]]['IP'])
            out.append(self.DictCatalog[uri[0]]['port'])
        elif uri[0] == "devicesList":
            if (len(query) != 0):
                for i in range (len(self.DictCatalog[uri[0]])):
                    if int(query['Num']) == int(self.DictCatalog[uri[0]][i]['deviceID']):
                        out.append(self.DictCatalog[uri[0]][i])
            else:
                for i in range (len(self.DictCatalog[uri[0]])):
                    out.append(self.DictCatalog[uri[0]][i]['deviceID'])
                    out.append(self.DictCatalog[uri[0]][i]['deviceName'])
        elif uri[0] == "usersList":
            if (len(query) != 0):
                for i in range (len(self.DictCatalog[uri[0]])):
                    if int(query['Num']) == int(self.DictCatalog[uri[0]][i]['userID']):
                        out.append(self.DictCatalog[uri[0]][i])
            else:
                for i in range (len(self.DictCatalog[uri[0]])):
                    out.append(self.DictCatalog[uri[0]][i]['userID'])
                    out.append(self.DictCatalog[uri[0]][i]['userName'])
        elif uri[0] == "greenhousesList":
            pass
        else:
            raise cherrypy.HTTPError(400, "ERROR: error with the parameters")
        return out

    def PUT(self, *uri, **query): #update device
        if uri[0] == "devicesList":
            pass
        elif uri[0] == "usersList":
            pass
        elif uri[0] == "greenhousesList":
            pass
        else:
            raise cherrypy.HTTPError(400, "ERROR: error with the parameters")
        return "Update done succesfully"

    def POST(self, *uri, **query): #adding device
        InputAsDict = json.loads(cherrypy.request.body.read())
        #passaggio ad una def per controllare che sia tutto corretto?
        if uri[0] == "devicesList":
           self.DictCatalog[uri[0]].append(InputAsDict)
        elif uri[0] == "usersList":
            self.DictCatalog[uri[0]].append(InputAsDict)
        elif uri[0] == "greenhousesList":
            self.DictCatalog[uri[0]].append(InputAsDict)
        else:
            raise cherrypy.HTTPError(400, "ERROR: error with the parameters")
        json.dumps(self.DictCatalog)
        return "Update done succesfully"

    def DELETE(self, *uri, **query):
        if uri[0] == "devicesList":
            pass
        elif uri[0] == "usersList":
            pass
        elif uri[0] == "greenhousesList":
            pass
        else:
            raise cherrypy.HTTPError(400, "ERROR: error with the parameters")
        return "Update done succesfully"

# This is the main of our program
if __name__ =="__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    webService = GreenHouseCatalog()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
