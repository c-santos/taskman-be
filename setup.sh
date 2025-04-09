set -e
set -x

docker compose down;
docker compose up --build -d;
docker compose run --rm taskman python manage.py migrate;
docker compose logs -f;
