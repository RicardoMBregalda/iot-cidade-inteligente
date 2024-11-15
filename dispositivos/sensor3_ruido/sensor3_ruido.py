# sensor3_ruido.py

import paho.mqtt.client as mqtt
import time
import random
import json

# Configurações do MQTT
broker = "localhost"
port = 1883
access_token = "uFQjmpJEa2gCz5VNGp0y"  # Substitua pelo Access Token do Sensor de Ruído
topic = "v1/devices/me/telemetry"

# Função para eliminar outliers
def process_data(data):
    if 30 <= data <= 120:  # Intervalo válido para ruído em decibéis (dB)
        return round(data, 2)
    else:
        return None

# Configuração do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(access_token)
client.connect(broker, port, 60)
client.loop_start()

print("Sensor de Ruído conectado ao broker MQTT.")

try:
    while True:
        # Simular leitura de sensor
        raw_data = random.uniform(10, 130)  # Gera dados aleatórios
        processed_data = process_data(raw_data)
        
        if processed_data is not None:
            payload = {"ruido": processed_data}
            client.publish(topic, json.dumps(payload))
            print(f"Dados enviados: {payload}")
        else:
            print(f"Outlier detectado (Ruído): {raw_data:.2f} dB")
        
        time.sleep(5)  # Intervalo entre envios (5 segundos)
except KeyboardInterrupt:
    print("Interrompendo o envio de dados do Sensor de Ruído.")
    client.loop_stop()
    client.disconnect()
