from flask import Flask
from flasgger import Swagger
from src.configs.config import get_config
from src.controllers.healthcontroller import health_controller_initialize
from src.controllers.controller import SearchController, controller_initialize

def main():
    app = Flask(__name__)
    get_config()
    health_controller_initialize(app)
    search_controller = SearchController()
    controller_initialize(app, search_controller)
    app.run(port=get_config().port, debug= True)

try:
    main()
except Exception as ex:
    print(ex)