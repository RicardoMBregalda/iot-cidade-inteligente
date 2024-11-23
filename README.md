# IoT Cidade Inteligente

## Descrição
Projeto para criação de um ambiente de Internet das Coisas (IoT) distribuído, com 4 dispositivos enviando dados de sensoriamento ambiental para uma aplicação em nuvem (ThingsBoard). Os dados são processados e visualizados em um dashboard, com ações executadas com base em condições específicas.

## Estrutura do Projeto
- **Dispositivos:**
  - `sensor1_temperatura.py` - Temperatura
  - `sensor2_umidade.py` - Umidade
  - `sensor3_ruido.py` - Ruído
  - `sensor4_qualidade_ar.py` - Qualidade do Ar

- **Aplicação para visualização dos Dashboards:**
  - ThingsBoard (localhost:8080)

## Como clonar o projeto
```bash
  git clone https://github.com/RicardoMBregalda/iot-cidade-inteligente.git
```
## Como realizar a instalação do projeto (Windows)
Para que o projeto seja funcional, primeiramente deve ser realizado a instalação do Python3 e Docker.
- Link de download do Python3: https://www.python.org/downloads/
- Link de download do Docker: https://docker-docs.uclv.cu/get-docker/

### Instalação da Biblioteca do MQTT
```bash
pip install paho-mqtt
```

### Instalação do ThingsBoard (Windows + Docker)

```bash
docker volume create mytb-data
```
```bash
docker volume create mytb-logs
```
Após a criação dos volumes, deveremos acessar via terminal a `outros_arquivos` e rodar os seguintes comandos:

```bash
docker compose up -d
```
```bash
docker compose logs -f mytb
```
Para acessar o ThingsBoard deverá ser acessado seguinte link: localhost:8080.
Para acessar o painel adminstrativo deverá ser informado o usuario `tenant@thingsboard.org` com a senha `tenant`.

  