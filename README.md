# Readme

## Prerequisites

Docker, Java 17 SDK, Maven, Python 3, Kafka-Python:

```bash
pip install kafka-python
```

## How to run

Start Kafka, Flink and Kafdrop with docker compose:

```bash
docker compose up
```

Wait few seconds for Kafka to start and start producer in another terminal:

```bash
python3 producer/producer.py
```
Build Flink executable and deploy it on Flink cluster:

```bash
sh ./build_and_deploy_flink.sh
```

## How to monitor

Enter `localhost:9000` in a web browser. You will see Kafdrop interface where you can monitor Kafka messages.

![Screenshot from 2024-05-22 15-55-41](https://github.com/michaldudzisz/PSD-Lab-3/assets/49537887/0f65f0b9-1416-4298-9d8a-a133fe72acf6)
