from kafka import KafkaConsumer
from nlp.processor import process_message
import json

consumer = KafkaConsumer(
    'news',
    'tweets',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    msg = message.value
    print(f"Topic: {message.topic}")
    
    processed = process_message(msg)
    print("→", processed["sentiment"], "|", processed["entities"])
