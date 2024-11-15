# sensor2_umidade.py

import paho.mqtt.client as mqtt
import time
import random
import json

# Configurações do MQTT
broker = "localhost"
port = 1883
access_token = "Y2FERMhhEWzBa1mIbbBg"  # Substitua pelo Access Token do Sensor de Umidade
topic = "v1/devices/me/telemetry"

# Função para eliminar outliers
def process_data(data):
    if 0 <= data <= 100:  # Intervalo válido para umidade (%)
        return round(data, 2)
    else:
        return None

# Configuração do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(access_token)
client.connect(broker, port, 60)
client.loop_start()

print("Sensor de Umidade conectado ao broker MQTT.")

try:
    while True:
        # Simular leitura de sensor
        raw_data = random.uniform(-10, 110)  # Gera dados aleatórios
        processed_data = process_data(raw_data)
        
        if processed_data is not None:
            payload = {"umidade": processed_data}
            client.publish(topic, json.dumps(payload))
            print(f"Dados enviados: {payload}")
        else:
            print(f"Outlier detectado (Umidade): {raw_data:.2f}%")
        
        time.sleep(5)  # Intervalo entre envios (5 segundos)
except KeyboardInterrupt:
    print("Interrompendo o envio de dados do Sensor de Umidade.")
    client.loop_stop()
    client.disconnect()
