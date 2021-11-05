# Bakery Manager

A bakery manager portal API. Two main Apps, Admin(API, developed from scratch) and Customer.

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
#### Creating a superuser is neccessary as an admin can only populate the DB as well as create a new admin.
![image](https://user-images.githubusercontent.com/23053807/140507023-9d77f8f3-23ec-4554-a0ed-4e76b51ae572.png)

## Features
Bakery Shop ADMIN has the capability to:

1.       Register and Login (Only an admin can create a new admin)

2.       Add Ingredients like Milk, Eggs etc.

3.       Create Product from list of ingredients

4.       Get detail of Product (ingredients with quantity percentage, cost price, selling price etc.)

5.       Manage inventory

Customer or buyer have the capability to:

1.       Register and Login

2.       Get list of available products

3.       Place order and get bill

4.       See order history

# How to use

* Creating a superuser
* Logging in using the /login route. Use the auth-token in header for future requests.
* Use the postman.json documentation for further info on how to use the routes.
* In the start, you need to populate the DB, like add ingredients and products.
* Products, when first created dont have selling price, you need to update this info using the same route but with different Data in body (ref:postman.json).
* Then the market is ready to be used by customers.
