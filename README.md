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


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


### Database Setup (LOCAL)
This app is developed with postgre SQL in mind. By navigating the `/starter` directory,
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
 # Hosted URL


 # How to setup Authentication
 See explanation of Roles in the following section.
 
 RBAC Role token for Manager: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFOZDFNWk5pWWs2WUIzWjZscGJVRCJ9.eyJpc3MiOiJodHRwczovL21hdHRqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGQ0ZmQ3MjAzYTZlYTAwNzAxNTgyYzEiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYzMDI2MzEzMiwiZXhwIjoxNjMwMzQ5NTMyLCJhenAiOiJOYXdsV1RtRUJYbmxteUZicDQ1TkN2QU9KNGtmNEN6SSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmN1c3RvbWVyIiwiYWRkOmVtcGxveWVlIiwiYWRkOm1hbmFnZXIiLCJhZGQ6cmVzZXJ2YXRpb24iLCJhZGQ6dmVoaWNsZSIsImRlbGV0ZTp2ZWhpY2xlIiwiZ2V0OmN1c3RvbWVyIiwiZ2V0OmVtcGxveWVlIiwiZ2V0Om1hbmFnZXIiLCJnZXQ6cmVzZXJ2YXRpb24iLCJ1cGRhdGU6Y3VzdG9tZXIiLCJ1cGRhdGU6ZW1wbG95ZWUiLCJ1cGRhdGU6bWFuYWdlciIsInVwZGF0ZTpyZXNlcnZhdGlvbiIsInVwZGF0ZTp2ZWhpY2xlIl19.lkvx0sR_d6dp2Xz80tmYApalnU00Lfs7O7QYdc-LNz4et1UCcadMiKVhIZhk4XHUh9ogPhQz6U-qbFASXUI84qZp7y58xSixNoDz0a6VNA1I4vUBc21XNutIBhWu4EpYYKlc6Qbr6iXerTj0Yet-nIvFbXGh0j34QPPF-i5E1KfKjfocW2TooylxeXTvXTAoLTmsiM_OMBPFUKFNG6tzumHtTPCR9XcFZr8Z8CqRQ4X65ax7IIK5Pq55X1Sm6XbV5OX1JA-D76ks7A4CRvlWkzw2clymPCmKiM82IpuvjaiFDCmsUl0vaOVgwe7n-aqSRmZZeTvPtfRELeizzBWF0w

 RBAC Role token for Employee:
 
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

GET /vehicles/<id>
Returns a particular vehicle in the database
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

GET /customers
Returns a list of customers in the database
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

GET /employees
Returns a list of employees in the database
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

GET /managers
Returns a list of managers in the database
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

GET /reservations
Returns a list of reservations
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

POST /customers
Add a customer to the database
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

POST /employees
Add a employee to the database
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

POST /managers
Add a manager to the database
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

POST /reservations
Add a reseravation to the database
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

POST /vehicles
Add A vehicle to the database
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

PATCH /reservations/<id>
Update an existing reservation
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

PATCH /vehicles/<id>
Update a certain vehicle's information
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

DELETE /vehicles/<id>
Deleting a vehicle as long as it doesn't have an active reservation
Response Example: 
{
    "message": "Vehicle deleted",
    "success": 200
}