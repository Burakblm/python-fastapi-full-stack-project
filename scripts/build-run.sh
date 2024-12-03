
cd /home/burak/python-fastapi-full-stack-project

git pull

sudo docker-compose -f /home/burak/python-fastapi-full-stack-project/docker-compose-prod.yml down -v

sudo docker pull burakblm/python-full-stack-backend:latest

sudo docker-compose -f /home/burak/python-fastapi-full-stack-project/docker-compose-prod.yml up -d