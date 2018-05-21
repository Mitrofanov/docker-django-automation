# docker-django-automation

## Project structure

This project contains of 2 folders:

- docker
- kubernetes

`docker` folder consists of sample Django app and docker file (include docker-compose) to build dockerized app and also test it locally using docker compose

`kubernetes` folder consists of kubernetes config files, that will deploy such app to minikube. 

## Quick how-to

1) To locally build and test app:

* clone repo
* `cd docker-django-automation/docker`
* `docker-compose up --build`

This will bottstrap sample app + postgres container on your machine

2) To deploy to minikube:

* clone repo
* run `eval $(minikube docker-env)` to be able to use local images with minicube
* `cd docker-django-automation/docker`
* `docker build . -t todoapp:latest`
* `cd ../kubernetes/postgres/postgres_image/`
* `docker build . -t postgres_rebuilded:latest`
* `cd ..`
* start postgres pod `kubectl apply -f postgres.yaml`
* `cd ../todo_app/`
* start app pod `kubectl apply -f todo.yaml`
* open app `minikube service todoapp`


You should be able to use app

