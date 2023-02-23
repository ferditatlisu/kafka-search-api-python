from flask import Flask

def health_controller_initialize(app : Flask):
    @app.route('/_monitoring/health', methods = ['GET'])
    def health_get(): 
        return "OK"
    
