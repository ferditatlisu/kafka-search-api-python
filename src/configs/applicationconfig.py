import json
from dataclasses import dataclass

@dataclass
class Redis:
    host: str
    password: str
    database: int

@dataclass
class Kafka:
    host : str
    topicName : str

@dataclass
class ApplicationConfig:
    port : int
    kafka : Kafka
    redis : Redis