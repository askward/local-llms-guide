# Beginner Guide: Local LLMs With Ollama, Docker, And FastAPI

---

## Overview

This is a setup for running llms locally inside of a docker container and behind a FastAPI.

The API supports both full generation and streaming endpoints to hit.

The ollama-template folder is where you will find the FastAPI code as well as the Docker setup to get Ollama and the API up and running.

The ollama-test folder is a simple Docker container that you can spin up and run `main.py` in to test both the `/stream` endpoint and `/generate` endpoint of the API in the other container. 

These containers use a Docker network bridge to gain access to interact.

---

## Configuration

To change the LLM you are using locally go into the `.env` file inside ollama-template folder and update the `LLM` variable. This is default set to `llama3.2:3b` for a fast and small model for testing.

To change the embedding model you are using locally go into the `.env` file inside ollama-template folder and update the `EMBEDDING_MODEL` variable. This is set to `sentence_transformer` by default.

This guide does not support interactive chatting and is tested using a statically defined message in the ollama-test `main.py` file. If you wish to test with a different question just update the `message` string.

By default both the `/generate` test code and `/stream` test code are uncommented in the ollama-test `main.py` file. If you wish to do one test at a time you can simply comment out the few lines of code that handle either individual call.

---

## Instructions

To use commands for a specific container you have to be in the container's dir:
```
cd ollama-template

or 

cd ollama-test
```

To spin up a docker container using docker-compose use this command:
```
docker-compose up --build -d
```

To enter into a spun up container to run scripts use this command:
```
docker exec -it <container-name> bash
```

To run the main script inside of a container use these commands:
```
cd src

then

python3 main.py
```

To exit a spun up container after running tests use this command:
```
exit
```

To spin down a docker container using docker-compose use this command:
```
docker-compose down
```

---
