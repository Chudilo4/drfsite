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
