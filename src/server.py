from flask import Flask, Response
from datetime import datetime
from logger import Logger
from logic import FindIndex

logger = Logger()

################ EndpointAction ################
class EndpointAction(object):
    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        response, status_code = self.action()
        return Response(response, status=status_code, headers={})

################ FlaskAppWrapper ################
class FlaskAppWrapper(object):
    _app = None

    @property
    def App(self):
        return self._app

    def __init__(self, name):
        self._app = Flask(name)

    def run(self):
        self.App.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.App.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))


################ Server class ################
class Server():
    _app = None
    _data = {}
    _config = {}
    _miss_ratio = 0
    
    @property
    def MissRatio(self):
        return self._miss_ratio
    
    @property
    def Data(self):
        return self._data


    def __init__(self, config={}) -> None:
        global logger
        logger = Logger(config['LOG_LEVEL'])
        self._config = config
        self._miss_ratio=int(config['MISS_RATIO'])
        self.LoadData()

        self._app = FlaskAppWrapper('Finder Demo Server')
        self._RegisterServices()
        
    # registers all the services
    def _RegisterServices(self):
        self._app.add_endpoint(endpoint='/healthcheck', endpoint_name='healthcheck', handler=self.HealthCheck)
        self._app.add_endpoint(endpoint='/', endpoint_name='info', handler=self.Info)
        
        @self._app.App.route('/index/<target_value>', methods=['GET'])
        def SearchIndex(target_value):
            logger.INFO(f"/index/{target_value} - has been called")
            val = isinstance(target_value, int)
            try:
                value = int(target_value)
            except:
                logger.WARING(f"/index/{target_value} - has been called - Target value should be integer")
                return "{\"error\":\"Target value should be integer\"}", 400    

            result, exact = FindIndex(self.Data, value, self.MissRatio, logger=logger)
            return f"{result}", 200
    
    # data loader - loads the data from the configured data file
    def LoadData(self):
        input = self._config['INPUT_FILE']
        with open(input) as datasource: 
            self._data=datasource.read().splitlines()
        return True
    
    # Info endpoint - to be able to share usage info to the users
    def Info(self):
        logger.INFO(f"Info - has been called")
        return f"call /index/<target_value> - to search for the given index in the parsed data. <target_value> should be integer", 200

    # Starts the server
    def Run(self):
        self._app.run()
        return

    
    #HealthCheck function - to check if the server is healthy or not - mandatory for real services - eg.: for load balancers, or any orchestration
    def HealthCheck(self):
        now = datetime.now()
        return f"HealthCheck - OK {now}", 200
    