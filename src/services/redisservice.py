import json
from redis import ConnectionPool, Redis
from src.configs.config import get_config

class RedisService:
    redis_connection : Redis
    def __init__(self):
        pool = ConnectionPool(host=get_config().redis.host,
                          password=get_config().redis.password,
                          db=get_config().redis.database,
                          port= 6379)

        self.redis_connection = Redis(connection_pool=pool)
        
    def get_result(self, key: str):
        response = self.redis_connection.lrange(key, 0, 1000)
        response.reverse()
        return response
    
    def save_search(self, key: str):
        result = {"state" : "In queue"}
        value = json.dumps(result)
        self.redis_connection.rpush(key, value)
        
        return result
        
    def delete(self, key: str):
        self.redis_connection.delete(key)
    
    def get_lenght(self, key):
        return self.redis_connection.llen(key)