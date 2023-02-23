import json
import os
from dacite import from_dict
from src.configs.applicationconfig import ApplicationConfig


class ConfigurationManager:
    config : ApplicationConfig
    def __init__(self):
        env = os.getenv("ENVIRONMENT", "stage")
        with open(f'resources/application-{env}.json') as f:
            data = json.load(f)
            self.config = from_dict(data_class=ApplicationConfig, data= data)
            print(self.config)
        
    def get(self):
        return self.config
        

cfg = ConfigurationManager()        

def get_config():
    return cfg.config
