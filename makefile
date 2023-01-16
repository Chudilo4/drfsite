migrate:
	python manage.py makemigrations
	python manage.py migrate
dev:
	python manage.py runserver
shell:
	python manage.py shell
add_requirements:
	pip freeze > requirements.txt
install_requirements:
	pip install -r requirements.txt
start:	
	gunicorn -w 2 -b 77.79.185.10:8080 drfsite.wsgi
