### FSND_Capstone
A Web App about Car Rentals

 # Motivation
 Dealing and working on cars are one of my favorite hobbies/interests. It comes naturally to make my capstone project around the idea :)

 This is a "Car Rental" API. In it includes:
 - A well modeled relational database, including a ternany relationship
 - Appropriate styled REST API endpoints following the CRUD approach
 - API endpoints have different amount of authorization, Managers have access to all the endpoints, employees have access to most, while customers have no special access

### Installing Dependencies (LOCAL)

1. **Python 3.x** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the root directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


### Local Database setup
This app is developed with postgre SQL in mind. In the root directory,
there is a env setup file called "config.py". Update the following:

```
os.environ['DB_USER'] = 'my_username'
os.environ['DB_PASSWORD'] = 'my_password'
os.environ['DB_NAME'] = 'car_rental'
os.environ['TEST_DB_NAME'] = 'car_rental_test'
```

Hints:
- Your DB_USER and DB_PASSWORD should be updated to the most convenient credentials in your local system.  
- The values you give to DB_NAME and TEST_DB_NAME should also be used to create 2 seperate databases locally in order for the app to function. Like this:

```
psql -U <DB_USER>
(enter DB_PASSWORD)
create database <DB_NAME>;
create database <TEST_DB_NAME>;
```

### Flask APP Setup for development 

Please follow the steps above to create the database and link the app to your created postgre databases.
Then:
```
export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
```
Then use Postman to start pinging the endpoints below, including authorization when necessary, using your local server. 
For example:
```
http://127.0.0.1:5000/vehicles
```
### Flask APP Setup for unit testing
Please follow the steps above to create the database and link the app to your created postgre databases.
Then:
```
export FLASK_APP=app.py
export FLASK_ENV=development
python -m test_app
```


### Hosted URL
https://fsnd-capstone-j.herokuapp.com

Use this URL to ping the hosted web app

Example using Postman:
```
https://fsnd-capstone-j.herokuapp.com/vehicles
```

### Authentication/Authorization
 Bearer Tokens have been provided due to the implicit nature of this app. If a new user logged in, they would need to be granted a RBAC role to gain further access to the system.
 
 RBAC Role token for Manager: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFOZDFNWk5pWWs2WUIzWjZscGJVRCJ9.eyJpc3MiOiJodHRwczovL21hdHRqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDQwNzQzMjQ4NDE0MTE0NzkzNyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjMwMjk3ODExLCJleHAiOjE2MzAzODQyMTEsImF6cCI6Ik5hd2xXVG1FQlhubG15RmJwNDVOQ3ZBT0o0a2Y0Q3pJIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6Y3VzdG9tZXIiLCJhZGQ6ZW1wbG95ZWUiLCJhZGQ6bWFuYWdlciIsImFkZDpyZXNlcnZhdGlvbiIsImFkZDp2ZWhpY2xlIiwiZGVsZXRlOnZlaGljbGUiLCJnZXQ6Y3VzdG9tZXIiLCJnZXQ6ZW1wbG95ZWUiLCJnZXQ6bWFuYWdlciIsImdldDpyZXNlcnZhdGlvbiIsInVwZGF0ZTpjdXN0b21lciIsInVwZGF0ZTplbXBsb3llZSIsInVwZGF0ZTptYW5hZ2VyIiwidXBkYXRlOnJlc2VydmF0aW9uIiwidXBkYXRlOnZlaGljbGUiXX0.W2vq7cyO17aqk4B5RE6TIWxIZJszy6HV_JdgjFClWbYbki98MFu9-IgVjk6VyBQdjf5JX67N1g7_lRlhoiY8PNB89ayUL_kLK9X_FkUA3cjexFoLR2xRsnJtpnMgvnc0Kj1V2ZxiLIXvzwmU6Pv2fItyEXd2hcxTLUFMsUM5_0UnpVS6ZnKlXWL6pmlrLaKADcSS80j5ixCxMnxCX3bb_uDi5QvjwnlhYBqAuZi-gB_gn5ZVDxbfo0UzQOiI_j2OCpomCBGdpqFyjVVJIRpQK1VnEFzAlK2IyOzdutqbXlS9aD3ntxg0oo5CBiXJJBxLMt5USs1dSXwZs425somc7g

 RBAC Role token for Employee:
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFOZDFNWk5pWWs2WUIzWjZscGJVRCJ9.eyJpc3MiOiJodHRwczovL21hdHRqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGU5YzhlMDQ4NGVhNjAwNzA1OWY0MjYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYzMDI5Nzc2OCwiZXhwIjoxNjMwMzg0MTY4LCJhenAiOiJOYXdsV1RtRUJYbmxteUZicDQ1TkN2QU9KNGtmNEN6SSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmN1c3RvbWVyIiwiYWRkOnJlc2VydmF0aW9uIiwiZ2V0OmN1c3RvbWVyIiwiZ2V0OmVtcGxveWVlIiwiZ2V0Om1hbmFnZXIiLCJnZXQ6cmVzZXJ2YXRpb24iLCJ1cGRhdGU6Y3VzdG9tZXIiLCJ1cGRhdGU6ZW1wbG95ZWUiLCJ1cGRhdGU6cmVzZXJ2YXRpb24iXX0.bx3nj4DpciD4xrETV4qRRTPKiZZPYm-8CZkRoSqOHHOYB2YhwquemMVKTxcGx2xk-HNrLABIrmUqtW_euTo3Kpis9GH-bVm4vx_ISyjIZsKGmuRi0_WLBhw06KFFxUfXcj2XFBlr9NZZD6yUSSh0oCp-Ewm7KSZIVWjbzDBd8ifCpUq8pa54DCA8I1v-92YDpnMSF8DUql1d6u-qJvF9Ls0RXf9vOTr5JsdrFjswnehz4LODOurmYg3Hd5Bou6c3Ask84WRof4MYQfERU59DBMe-LsthghGjzy4QjrCdylzYGB5DtJTbTl1K3ZV_2VVi9URVzeghISUdf0j35Avt3A
 
 RBAC Role token for Customer:  
 N/A

 # Defined Roles and their Permissions

Low-tier Role: Customer 

    Permissions: 
    - None

    Endpoints available for access:
    - GET /vehicles
    - GET /vehicles/<id>

    Notes: Customers do not effectively have any RBAC-defined role. They can ping
           the Car Rental database to see what cars are available for rental only.

Mid-tier Role: Employee

*Includes all privileges of Customers

    Permissions: 
    - get:customer
    - get:employee
    - get:manager
    - get:reservation
    - add:customer
    - add:reservation
    - update:reservation

    Endpoints available for access:
    - GET /customers
    - GET /employees
    - GET /managers
    - GET /reservations
    - POST /customers
    - POST /reservations
    - PATCH /reservations/<id>

    Notes: Employees can facilitate logic up-keep of the car rental business. 
           They can add customers and create, reference, and update reservations


Highest-tier Role: Manager

*Includes all privileges of Employees

    Permissions: 
    - add:employee
    - add:manager
    - add:vehicle
    - update:vehicle
    - delete:vehicle

    Endpoints available for access:
    - POST /employees
    - POST /managers
    - POST /vehicles
    - PATCH /vehicles/<id>
    - DELETE /vehicles/<id>

    Notes: Managers can use any available endpoint. Highlights are adding,
    updating, and deleting vehicles. They can also add staff to the database.

# API Endpoint Description
Total list:
    - GET /vehicles
    - GET /vehicles/<id>
    - GET /customers
    - GET /employees
    - GET /managers
    - GET /reservations
    - POST /customers
    - POST /reservations
    - POST /employees
    - POST /managers
    - POST /vehicles
    - PATCH /reservations/<id>
    - PATCH /vehicles/<id>
    - DELETE /vehicles/<id>


GET /vehicles
Returns a list of vehicles in the database
```
{
    "message": "OK",
    "success": 200,
    "vehicles": [
        {
            "body_style": "pickup",
            "color": "blue",
            "currently_rented": false,
            "id": 1,
            "make": "Ford",
            "model": "F-150",
            "year": 2020
        }
    ]
}
```
GET /vehicles/<id>
Returns a particular vehicle in the database
```
{
    "message": "OK",
    "success": 200,
    "vehicle": {
        "body_style": "pickup",
        "color": "blue",
        "currently_rented": false,
        "id": 1,
        "make": "Ford",
        "model": "F-150",
        "year": 2020
    }
}
```
 
GET /customers
Returns a list of customers in the database
```
{
    "customers": [
        {
            "address": "Somewhere in Kansas",
            "first_name": "Sivaram",
            "id": 1,
            "last_name": "Shukla",
            "type": "customer"
        }
    ],
    "message": "OK",
    "success": 200
}
```
 
GET /employees
Returns a list of employees in the database
```
{
    "employees": [
        {
            "address": "Somewhere in Canton",
            "first_name": "Morgan",
            "id": 2,
            "last_name": "London",
            "manager_id": 1,
            "type": "employee"
        }
    ],
    "message": "OK",
    "success": 200
}
```
 
GET /managers
Returns a list of managers in the database
```
{
    "managers": [
        {
            "address": "Somewhere in Seattle",
            "first_name": "Matt",
            "id": 1,
            "last_name": "London",
            "type": "manager"
        }
    ],
    "message": "OK",
    "success": 200
}
```

GET /reservations
Returns a list of reservations
```
{
    "message": "OK",
    "reservations": [
        {
            "cost": 50.0,
            "customer_name": "Shivam Shukla",
            "employee_name": "Morgan London",
            "id": 1,
            "reservation_open": true,
            "vehicle_id": 1,
            "vehicle_make_and_model": "Chevrolet Silverado"
        }
    ],
    "success": 200
}
```

POST /customers
Add a customer to the database
```
Request example:
{
    "first_name": "Sivaram",
    "last_name": "Shukla",
    "address": "Somewhere in Kansas"
}
Response:
{
    "message": "Customer added",
    "success": 201
}
```

POST /employees
Add a employee to the database
```
Request example:
{
    "first_name": "Richard",
    "last_name": "Doreen",
    "address": "Somewhere in Alden",
    "manager_id": 1
}
Response:
{
    "message": "Employee added",
    "success": 201
}
```
 
POST /managers
Add a manager to the database
```
Request example:
{
    "first_name": "Matt",
    "last_name": "London",
    "address": "Somewhere in Seattle"
}
Response:
{
    "message": "Manager added",
    "success": 201
}
```

POST /reservations
Add a reseravation to the database
```
request example:
{
    "vehicle_id": 1,
    "customer_id": 1,
    "employee_id": 2,
    "cost": 50.00
}
response example:
{
    "message": "Reservation added",
    "success": 201
}
```

POST /vehicles
Add A vehicle to the database
```
Request Example:
{
    "make": "Ford",
    "model": "F-150",
    "year": "2020",
    "body_style": "pickup",
    "color": "blue"
}
Response
{
    "message": "Vehicle added",
    "success": 201
}
```
 
PATCH /reservations/<id>
Update an existing reservation
```
Request example:
{
    "cost" : 45.00
}
Response example:
{
    "message": "Reservation updated",
    "success": 200,
    "updated_vehicle": [
        {
            "cost": 45.0,
            "customer_name": "Shivam Shukla",
            "employee_name": "Morgan London",
            "id": 1,
            "reservation_open": true,
            "vehicle_id": 1,
            "vehicle_make_and_model": "Chevrolet Silverado"
        }
    ]
}
```

PATCH /vehicles/<id>
Update a certain vehicle's information
```
Request example:
{
    "make" : "Chevrolet",
    "model" : "Silverado"
}
Response:
{
    "message": "Vehicle updated",
    "success": 200,
    "updated_vehicle": [
        {
            "body_style": "pickup",
            "color": "blue",
            "currently_rented": true,
            "id": 1,
            "make": "Chevrolet",
            "model": "Silverado",
            "year": 2020
        }
    ]
}
```

DELETE /vehicles/<id>
Deleting a vehicle as long as it doesn't have an active reservation
```
Response Example: 
{
    "message": "Vehicle deleted",
    "success": 200
}
```
