This repo provides a docker image for containers running an elasticsearch app. The container will wait on an ES instance to be ready, before starting the main python app.

# Setup
You can either clone this repo and build it by yourself or you can use the image shuewe/es-python-app from docker hub.
# Example use case
The following docker-compose file creates three containers:
- An elasticsearch container
- A kibana instance running on localhost:5601
- An container which starts an app (my_app.py) when elasticsearch is ready

Make sure docker can access at least the port 5601 from localhost. Otherwise kibana won't work. (This should work on Ubuntu and Windows 10 Pro, for Windows 10 home, with Docker Quickstart Terminal, you have to configure the VirtualBox VM).
Assure, that docker has enough memory. Elasticsearch / Kibana need >4GB.
```docker
version: '3'
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.8.0
    container_name: es
    environment:
      - discovery.type=single-node
    volumes:
      - data01:/usr/share/elasticsearch/data
    ports:
        - 9200:9200
        - 9300:9300
    networks: 
      - elastic

  kib01:
    image: docker.elastic.co/kibana/kibana:7.8.0
    container_name: kib01
    ports:
      - 5601:5601
    environment:
      - "ELASTICSEARCH_HOSTS=http://es:9200"
      #- "SERVER_HOST=192.168.99.100"
    networks: 
      - elastic

  app:
    image: shuewe/es-python-app
    container_name: es-app
    environment: 
      - ES_HOST=es
      #- ES_PORT=9200
    volumes: 
      - ./appData/:/script
    networks: 
      - elastic
    working_dir: /script
    command: python my_app.py

volumes:
  data01:
    driver: local

networks:
    elastic:
        driver: bridge
```