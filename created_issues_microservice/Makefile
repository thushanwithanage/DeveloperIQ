install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
build:
	#build container
	docker build -t created_issues_microservice_image .
run:
	#run docker
	docker run -p 127.0.0.1:8081:8081 3a50d662e79f