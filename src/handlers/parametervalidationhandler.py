from typing import Dict

class ParameterValidationHandler():
    def __init__(self, dict : Dict):
        self.dict = dict
        
    def handle(self):
        self.topic_name = self.dict.get("topicName", None)
        self.key = self.dict.get("key", None)
        self.value = self.dict.get("value", None)
        if not self.topic_name or (not self.key and not self.value):
            return False
        
        return True