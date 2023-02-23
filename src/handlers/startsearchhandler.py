import json
from typing import Dict
from src.dto.searchdata import SearchData
from src.services.kafkaservice import KafkaService
from src.services.redisservice import RedisService

class StartSearchHandler():
    def __init__(self, producer : KafkaService, redis: RedisService, data : Dict):
        self.producer = producer
        self.redis = redis
        self.data= SearchData(data)
        
    def handle(self):
        results = self.redis.get_result(self.data.id)
        if len(results) == 0:
            return self.start_search()
        else:
            return self.get_active_search_result(results)
        
    def start_search(self):
        result =self.redis.save_search(self.data.id)
        self.producer.send(self.data)
        return self.data.id, [result]
    
    def get_active_search_result(self, results):
        res = []
        for result in results:
            res.append(json.loads(result.decode('UTF-8')))
            
        return self.data.id, res