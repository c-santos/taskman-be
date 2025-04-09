set -e
set -x

docker compose down
docker compose up -d

docker compose run --rm taskman python manage.py migrate

docker compose logs -f
