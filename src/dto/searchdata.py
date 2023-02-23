import json
from typing import Dict, Optional

class SearchData:
    topic_name : str
    key : Optional[str]
    value : Optional[str]
    
    def __init__(self, dict: Dict):
        self.topic_name = dict.get("topicName", None)
        self.key = dict.get("key", None)
        self.value = dict.get("value", None)
        self.id = self.topic_name
        if self.key:
            self.id += f'k-{self.key}' 
        if self.value:
            self.id += f'v-{self.value}'
        
    def to_json(self):
        return json.dumps(self.__dict__)