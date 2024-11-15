# sensor1_temperatura.py

import paho.mqtt.client as mqtt
import time
import random
import json

# Configurações do MQTT
broker = "localhost"  # Broker local
port = 1883
access_token = "fHExHQCBsD99CqHGRnrm"  # Substitua pelo Access Token do Sensor de Temperatura
topic = "v1/devices/me/telemetry"

# Função para eliminar outliers
def process_data(data):
    if -20 <= data <= 50:  # Intervalo válido para temperatura em Celsius
        return round(data, 2)
    else:
        return None

# Configuração do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(access_token)
client.connect(broker, port, 60)
client.loop_start()

print("Sensor de Temperatura conectado ao broker MQTT.")

try:
    while True:
        # Simular leitura de sensor
        raw_data = random.uniform(-30, 60)  # Gera dados aleatórios
        processed_data = process_data(raw_data)
        
        if processed_data is not None:
            payload = {"temperatura": processed_data}
            client.publish(topic, json.dumps(payload))
            print(f"Dados enviados: {payload}")
        else:
            print(f"Outlier detectado (Temperatura): {raw_data:.2f}°C")
        
        time.sleep(5)  # Intervalo entre envios (5 segundos)
except KeyboardInterrupt:
    print("Interrompendo o envio de dados do Sensor de Temperatura.")
    client.loop_stop()
    client.disconnect()
