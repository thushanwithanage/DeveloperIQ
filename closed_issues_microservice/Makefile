install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
build:
	#build container
	docker build -t closed_issues_microservice_image .
run:
	#run docker
	docker run -p 127.0.0.1:8082:8082 6e53fcc38855