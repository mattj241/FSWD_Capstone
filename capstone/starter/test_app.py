import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import *

MANAGER_TOKEN = os.getenv('MANAGER_TOKEN')
EMPLOYEE_TOKEN = os.getenv('EMPLOYEE_TOKEN')

class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = os.getenv('TEST_DB_NAME')
        database_username = os.getenv('DB_USER') 
        database_password = os.getenv('DB_PASSWORD') 
        self.database_path = "postgresql://{}:{}@{}/{}"\
            .format(database_username,
                    database_password,
                    'localhost:5432',
                    self.database_name)
        setup_db(self.app, self.database_path)
        
        self.new_vehicle = {
            "make": "Ford",
            "model": "F-150",
            "year": "2020",
            "body_style": "pickup",
            "color": "blue"
        }

        self.new_vehicle_2 = {
            "make": "Ferrari",
            "model": "F50",
            "year": "2005",
            "body_style": "exotic",
            "color": "Rosa Corsa"
        }

        self.new_vehicle_error = {
            "make": "Ford",
            "model": "F-150",
            "license_plate": "1KZ RTY",
        }

        self.new_customer = {
            "first_name": "Sivaram",
            "last_name": "Shukla",
            "address": "Somewhere in Ontario, Canada"
        }

        self.new_customer_error = {
            "first_name": "Sivaram",
            "last_name": "Shukla",
            "currently_renting" : False
        }

        self.new_manager = {
            "first_name": "Matt",
            "last_name": "London",
            "address": "Somewhere in Seattle"
        }

        self.new_employee = {
            "first_name": "Morgan",
            "last_name": "London",
            "address": "Somewhere in Canton",
            "manager_id": 1
        }

        self.new_employee_error = {
            "first_name": "Morgan",
            "last_name": "London",
            "address": "Somewhere in Ohio",
            "manager_id": 499
        }

        self.new_reservation = {
            "vehicle_id": 1,
            "customer_id": 1,
            "employee_id": 1,
            "cost": 50.00
        }

        self.new_reservation_error = {
            "vehicle_id": 1,
            "customer_id": 420,
            "employee_id": 69,
            "cost": 50.00
        }

        self.patch_vehicle = {
          "make": "Chevrolet",
          "model":"Silverado"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def test_adding_vehicles(self):
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client()\
            .post('/vehicles', json=self.new_vehicle, headers=headers)
        self.assertEqual(res.status_code, 201)

    def test_adding_vehicles_error(self):
        # the json obj "self.new_vehicle_error" is missing keys, 
        # will cause a failure
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client()\
            .post('/vehicles', json=self.new_vehicle_error, headers=headers)
        self.assertEqual(res.status_code, 422)

    def test_vehicles(self):
        res = self.client().get('/vehicles')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_vehicles_error(self):
        # Unlikely ID of unique vehicle in the DB, causing a lookup error
        res = self.client().get('/vehicles/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_bad_request(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 400)

    def test_adding_customer(self):
        headers = {"Authorization":EMPLOYEE_TOKEN}
        res = self.client().post('/customers',
                                 json=self.new_customer,headers=headers)
        self.assertEqual(res.status_code, 201)

    def test_adding_customer_error(self):
        # the json obj "self.new_vehicle_error" is missing keys, 
        # will cause a failure
        headers = {"Authorization":EMPLOYEE_TOKEN}
        res = self.client().post('/customers',
                                 json=self.new_customer_error,headers=headers)
        self.assertEqual(res.status_code, 422)
    
    def test_get_customers(self):
        headers = {"Authorization":EMPLOYEE_TOKEN}
        res = self.client().get('/customers', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_adding_manager(self):
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client().post('/managers',
                                 json=self.new_manager,headers=headers)
        self.assertEqual(res.status_code, 201)

    def test_adding_manager_error(self):
        # Requesting to add a manager with an employee token will fail
        headers = {"Authorization":EMPLOYEE_TOKEN}
        res = self.client().post('/managers',
                                 json=self.new_manager,headers=headers)
        self.assertEqual(res.status_code, 403)

    def test_get_managers(self):
        headers = {"Authorization":EMPLOYEE_TOKEN}
        res = self.client().get('/managers', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_adding_employee(self):
        headers = {"Authorization":MANAGER_TOKEN}
        manager_search = Manager.query.first()
        if manager_search is None:
            res = self.client().post('/managers',
                            json=self.new_manager,headers=headers)
            manager_search = Manager.query.first()
            db.session.expunge(manager_search)
            my_json=({
            "first_name": "Morgan",
            "last_name": "London",
            "address": "Somewhere in Canton",
            "manager_id": manager_search.id
            })
        res = self.client().post('/employees',
                                 json=my_json,headers=headers)
        self.assertEqual(res.status_code, 201)

    def test_adding_employee_error(self):
        # Employees require a foreign key to their manager, 
        # unlikely there is manager #499 in the database
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client().post('/employees',
                                 json=self.new_employee_error,headers=headers)
        self.assertEqual(res.status_code, 422)

    def test_get_employees(self):
        headers = {"Authorization":EMPLOYEE_TOKEN}
        res = self.client().get('/customers', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_adding_reservation(self):
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client().post('/customers',
                                json=self.new_customer,headers=headers)
        customer = Customer.query.first()
        db.session.expunge(customer)
        res = self.client().post('/employees',
                                json=self.new_employee,headers=headers)
        employee = Employee.query.first()
        db.session.expunge(employee)

        res = self.client().post('/vehicles',
                                json=self.new_vehicle,headers=headers)
        vehicle = Vehicle.query.first()
        db.session.expunge(vehicle)
        res = self.client().post('/reservations', headers=headers,
                                 json={
                                     "cost" : 50.00,
                                     "customer_id" : customer.id,
                                     "employee_id" : employee.id,
                                     "vehicle_id"  : vehicle.id
                                 })
        self.assertEqual(res.status_code, 201)

    def test_adding_reservation_error(self):
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client().post('/reservations',
         json=self.new_reservation_error, headers=headers)
        self.assertEqual(res.status_code, 422)

    def test_get_reservations(self):
        headers = {"Authorization":EMPLOYEE_TOKEN}
        res = self.client().get('/reservations', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_update_vehicle(self):
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client().patch('/vehicles/1',
                                  headers=headers,json=self.patch_vehicle)
        self.assertEqual(res.status_code, 200)

    def test_update_vehicle_error(self):
        # Patching vehicle that does not exist
        headers = {"Authorization":MANAGER_TOKEN}
        res = self.client().patch('/vehicles/0',
                                  headers=headers,json=self.patch_vehicle)
        self.assertEqual(res.status_code, 404)

    def test_delete_vehicle(self):
        headers = {"Authorization":MANAGER_TOKEN}
        # vehicle_with_no_reservation = \
        #     Vehicle.query.filter(Vehicle.currently_rented==False).first()
        res = self.client()\
                .post('/vehicles', headers=headers, json=self.new_vehicle_2)
        vehicle = Vehicle.query.filter(Vehicle.make=="Ferrari").first()
        # vehicle_with_no_reservation = \
        # Vehicle.query.filter(Vehicle.currently_rented==False).first()
        url = '/vehicles/'+str(vehicle.id)
        res = self.client().delete(url,headers=headers)
        self.assertEqual(res.status_code, 200)

    def test_delete_vehicle_error(self):
        # Deleting a vehicle with a reservation
        headers = {"Authorization":MANAGER_TOKEN}
        url = '/vehicles/0'
        res = self.client().delete(url,headers=headers)
        self.assertEqual(res.status_code, 404)

if __name__ == "__main__":
    unittest.main()