mkdir microservices
touch microservices/Docker-compose.yaml
################## First Service #########################
mkdir -p microservices/service1/app/templates
touch microservices/service1/Dockerfile
touch microservices/service1/app/app.py
touch microservices/service1/app/requirements.txt
touch microservices/service1/app/templates/index.html
touch microservices/service1/app/templates/test_service.html
################## Second Service #########################
mkdir -p microservices/service2/app
touch microservices/service2/Dockerfile
touch microservices/service2/app/app.py
touch microservices/service2/app/requirements.txt
