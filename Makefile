COMPOSE = docker-compose

down:
	$(COMPOSE) down

up: down
	$(COMPOSE) up

build: down
	$(COMPOSE) build