COMPOSE = docker-compose

down:
	$(COMPOSE) down

up: down
	$(COMPOSE) up

build: down
	$(COMPOSE) build

flask:
	$(COMPOSE) run backend flask $(cmd) $(args)
