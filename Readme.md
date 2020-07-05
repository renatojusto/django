sudo docker-compose run web django-admin startproject maratonafullcycle .

python manage.py migrate

django-admin startapp app

python manage.py makemigrations

python manage.py makemigrations --empty app

docker run -p 8000:8000 renatoalejusto/maratonafullcycle_web:latest

docker push renatoalejusto/maratonafullcycle_web:latest

docker tag maratonafullcycle_web:latest renatoalejusto/maratonafullcycle_web:latest

docker pull renatoalejusto/maratonafullcycle_web:latest

docker build . -t maratonafullcycle_web