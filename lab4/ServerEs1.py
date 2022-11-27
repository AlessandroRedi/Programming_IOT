import json
import cherrypy
import Es1 as reader


class Sensor(object):
    exposed = True

    def GET(self,*uri):
        oper = reader.DeviceManager()
        if uri[0] == "temperature":
            oper.temperature()
            pass
        elif uri[0] == "humidity":
            pass
        elif uri[0] == "both":
            pass
        else:
            output = "Command Error"
        return output

if __name__ == "__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    webService = Sensor()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()