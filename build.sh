#!/bin/sh

pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 populate_catalog.py

python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('alumnodb', 'admin@myproject.com', 'alumnodb')"

