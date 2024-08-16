# /real_time_processing/kafka_streaming.py

from kafka import KafkaConsumer
import json

class KafkaStreaming:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='lekuntuai-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def consume_stream(self):
        for message in self.consumer:
            data = message.value
            print(f"Received data: {data}")  # Example processing step

# Usage
kafka_stream = KafkaStreaming(topic="fraud_detection")
kafka_stream.consume_stream()
