from kafka import KafkaProducer
from src.configs.config import get_config
from src.dto.searchdata import SearchData


class KafkaService:
    producer : KafkaProducer
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=get_config().kafka.host)
     
    def send(self, search_data: SearchData):
        try:
            self.producer.send(topic=get_config().kafka.topicName, value=bytearray(search_data.to_json(), "utf-8"))
        except Exception as ex:
            print(ex)