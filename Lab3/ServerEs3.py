import json
import Es3 as bikesharing
import cherrypy


class HelloWorld(object):
    exposed = True

    def POST(self):
        bodyAsString = cherrypy.request.body.read()
        bodyAsDictionary = json.loads(bodyAsString)
        bike = bikesharing.DeviceManager("https://www.bicing.barcelona/en", bodyAsDictionary)
        return bike.out()


if __name__ == "__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    webService = HelloWorld()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
