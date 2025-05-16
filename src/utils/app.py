from flask import Flask
from flask_cors import CORS

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import config

#ROUTES
from routes import Productos

app=Flask(__name__)

#http://localhost:9300 el numero de puerto depende de lenguaje para front
CORS(app,resources={"*":{"origins":"http://localhost:9300"}})


def page_not_found(error):
    return "<h1>Página no encontrada</h1>",404
    

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    #BluePrints
    app.register_blueprint(Productos.main,url_prefix='/api/productos')
    
    #Error handlers
    app.register_error_handler(404,page_not_found)
    app.run()



