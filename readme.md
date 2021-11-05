# Bakery Manager

To install

* `Create a venv (virtual environment) with "Python 3.7" `
* `Install dependencies using requirements.txt` 
```
pip install -r requirments.txt
```

* `CD to the working directory (where 'manage.py' is), and then`
```bash
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py createsuperuser
python ./manage.py runserver
```

### Alternative Install (Using Docker)

```
docker build -t bakery-manager .
docker run --name instanceOne -d -p 8000:8000 bakery-manager:latest
docker exec -it instanceOne sh
python manage.py createsuperuser
```