
cd /home/burak/python-fastapi-full-stack-project

git pull

export POSTGRES_SERVER=${POSTGRES_SERVER}
export POSTGRES_PORT=${POSTGRES_PORT}
export POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
export POSTGRES_DB=${POSTGRES_DB}
export POSTGRES_USER=${POSTGRES_USER}
export ALGORITHM=${ALGORITHM}

sudo docker compose -f /home/burak/python-fastapi-full-stack-project/docker-compose-prod.yml down -v

sudo docker pull burakblm/python-full-stack-backend:latest

sudo docker compose -f /home/burak/python-fastapi-full-stack-project/docker-compose-prod.yml up -d