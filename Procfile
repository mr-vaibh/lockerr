release: python3 manage.py makemigrations
release: python3 manage.py migrate
web: gunicorn longerr.wsgi --preload --log-file -