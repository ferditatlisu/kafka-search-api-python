from flask import Flask, request
from src.handlers.parametervalidationhandler import ParameterValidationHandler
from src.handlers.clearhandler import ClearHandler
from src.services.redisservice import RedisService
from src.handlers.startsearchhandler import StartSearchHandler
from src.services.kafkaservice import KafkaService

class SearchController():
    def __init__(self):
        self.kafka_producer = KafkaService()
        self.redis_service = RedisService()

def controller_initialize(app: Flask, controller: SearchController):
    #query-parameters: topicName, key, value
    @app.route('/search', methods = ['GET'])
    def search(): 
        query_parameters = request.args.to_dict()
        validation = ParameterValidationHandler(query_parameters)
        is_valid = validation.handle()
        if not is_valid:
            return { 'message' : "topicName or (key or value) is empty"}
        
        handler = StartSearchHandler(controller.kafka_producer, 
                                     controller.redis_service, 
                                     query_parameters)
        
        queue_id, res = handler.handle()
        return {"id" : queue_id, "messages" : res}
    
    
    @app.route('/clear/<id>', methods = ['GET'])
    def clear(id: str): 
        ClearHandler(controller.redis_service, id).handle()
        return {"message" : "OK"}