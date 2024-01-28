MODEL_FILE = ./models/model-2022-01.bin
export MODEL_FILE

VERSION = 2022-01-v1
export VERSION

run:
	pipenv run python duration_prediction_serve/serve.py

docker_build:
	docker build -t duration-prediction:latest .

docker_run: docker_build
	docker run -it -p 9696:9696 --rm duration-prediction:latest