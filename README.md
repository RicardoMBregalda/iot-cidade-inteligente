# IoT Cidade Inteligente

## Descrição
Projeto para criação de um ambiente de Internet das Coisas (IoT) distribuído, com 4 dispositivos enviando dados de sensoriamento ambiental para uma aplicação em nuvem (ThingsBoard). Os dados são processados e visualizados em um dashboard, com ações executadas com base em condições específicas.

## Estrutura do Projeto
- **Dispositivos:**
  - `sensor1_temperatura.py` - Temperatura
  - `sensor2_umidade.py` - Umidade
  - `sensor3_ruido.py` - Ruído
  - `sensor4_qualidade_ar.py` - Qualidade do Ar

- **Broker MQTT:**
  - Mosquitto (localhost)

- **Aplicação em Nuvem:**
  - ThingsBoard (localhost:8080)
