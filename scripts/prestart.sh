
set -e
set -x

python app/backend_pre_start.py

cd app
alembic upgrade head
cd ..
