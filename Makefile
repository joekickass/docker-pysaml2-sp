.DEFAULT_GOAL := docker-build-run

PROXY = <set or remove me>
REPOSITORY = pysaml2
SERVICE_NAME = mysp
IMAGE = $(REPOSITORY)/$(SERVICE_NAME)

.PHONY: docker-build
docker-build:
	docker build --build-arg http_proxy=$(PROXY) --build-arg https_proxy=$(PROXY) --rm -t $(IMAGE):latest .

.PHONY: docker-run
docker-run:
	docker run --net="host" --rm -it $(IMAGE):latest

.PHONY: docker-build-run
docker-build-run: docker-build docker-run