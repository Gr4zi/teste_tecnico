# Stack ELK com Aplicação Geradora de Logs

## Descrição

Este projeto configura uma stack ELK (Elasticsearch, Logstash e Kibana) utilizando Docker Compose. Inclui uma aplicação simples em Python que gera logs e os envia para o Logstash.

## Estrutura do Projeto

- **app/**: Contém o código-fonte da aplicação geradora de logs.
- **logstash.conf**: Configuração do Logstash para processar e enviar logs para o Elasticsearch.
- **docker-compose.yml**: Arquivo de orquestração que define os serviços do Elasticsearch, Logstash, Kibana e a aplicação.

## Como Executar

1. **Construa e inicie os contêineres:**
   ```bash
   docker-compose up --build
