from kafka import KafkaProducer
from random import randint
from datetime import datetime
import json
import time
import numpy as np


def kafka_producer():
    return KafkaProducer(
        bootstrap_servers='localhost:9094',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )


def generate_temperature():
    mean = 12
    std_dev = 9
    temperature = np.random.normal(mean, std_dev)
    return temperature


def generate_measurement():
    thermometer_id = randint(0, 10_000)
    timestamp = datetime.now()
    temperature = generate_temperature()
    return {
        'thermometerId': str(thermometer_id),
        'timestamp': timestamp.isoformat(),
        'temperature': str(temperature)
    }


if __name__ == '__main__':
    producer = kafka_producer()
    topic = 'Temperature'

    for i in range(1, 10_000):
        data = generate_measurement()
        producer.send(topic, value=data)
        print(f'Sent: {data}')
        time.sleep(1)

    producer.flush()
    producer.close()
