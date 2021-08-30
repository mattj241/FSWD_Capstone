import os
import enum
import time
from typing import Counter
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.expression import false, null
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint, Table, MetaData
from sqlalchemy.sql.sqltypes import Boolean, Float
from config import init_env_vars
Base = declarative_base()


init_env_vars()

### UNCOMMENT these below vars to enable for local

# database_name = os.getenv('DB_NAME') 
# database_username = os.getenv('DB_USER') 
# database_password = os.getenv('DB_PASSWORD')
# database_path = "postgresql://{}:{}@{}/{}"\
#   .format(database_username, database_password, 'localhost:5432', database_name)

# HEROKU REQUIREMENTS
database_path = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    while True:
        try:
            db.app = app
            db.init_app(app)
            db.create_all()
            # Migrate(app, db)
        except sqlalchemy.exc.IntegrityError:
            db.drop_all()
            time.sleep(5)
            # pass
        
    

def session_revert():
  db.session.rollback()

def session_close():
  db.session.close()

'''
Schema Configuration

'''
class Reservation (db.Model):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    # implemented the time attrib, if time allows
    # start_time = 
    # end_time = 
    cost = Column(Float, nullable=False)
    reservation_open = Column(Boolean, nullable=False)
    vehicle  = relationship('Vehicle', uselist=False, foreign_keys=[vehicle_id])
    customer = relationship('Customer', uselist=False, foreign_keys=[customer_id])
    employee = relationship('Employee', uselist=False, foreign_keys=[employee_id])

    def __init__(self, vehicle_id, customer_id,
                 employee_id, cost, reservation_open):
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.cost = cost
        self.reservation_open = reservation_open

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_cust_info(id):
        return Customer.query.filter_by(id=id).first()
    
    def get_emp_info(id):
        return Employee.query.filter_by(id=id).first()
    
    def get_veh_info(id):
        return Vehicle.query.filter_by(id=id).first()
    
    def format(self):
        customer = Reservation.get_cust_info(self.customer_id)
        employee = Reservation.get_emp_info(self.employee_id)
        vehicle = Reservation.get_veh_info(self.vehicle_id)
        return {
            'id' : self.id,
            'cost': self.cost,
            'customer_name': customer.first_name + ' ' + customer.last_name,
            'employee_name': employee.first_name + ' ' + employee.last_name,
            'vehicle_id': self.vehicle_id,
            'vehicle_make_and_model': vehicle.make + ' ' + vehicle.model,
            'reservation_open' : self.reservation_open
        }

class Vehicle(db.Model):
    __tablename__= 'vehicle'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    body_style = Column(String)
    color = Column(String)
    currently_rented = Column(Boolean, nullable=False)
    reservations = relationship('Reservation', back_populates='vehicle')

    def __init__(self, make, model, year, body_style, color,
                currently_rented):
        self.make = make
        self.model = model
        self.year = year
        self.body_style = body_style
        self.color = color
        self.currently_rented = currently_rented

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id' : self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'body_style': self.body_style,
            'color': self.color,
            'currently_rented': self.currently_rented,
        }

class Person(db.Model):
    # __tablename__= 'person'
    __abstract__ = True

    # id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name  = Column(String, nullable=False)
    address = Column(String, nullable=False)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_on':type,
        'polymorphic_identity':'person',
    }


class Customer(Person):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    reservations = relationship('Reservation', back_populates='customer')

    __mapper_args__ = {
        'polymorphic_identity':'customer'
    }

    def __init__(self, first_name, last_name, address, type):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.type = type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'address' : self.address,
            'type' : self.type,
        }


class Manager(Person):
    __tablename__ = 'manager'

    id = Column(Integer, primary_key=True)
    employees = relationship('Employee', back_populates='manager')

    __mapper_args__ = {
        'polymorphic_identity':'manager'
    }

    def __init__(self, first_name, last_name, address, type):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.type = type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'address' : self.address,
            'type' : self.type
        }

class Employee(Person, db.Model):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    manager_id = Column(Integer, ForeignKey('manager.id'))
    manager = relationship('Manager', back_populates='employees')
    reservations = relationship('Reservation', back_populates='employee')

    __mapper_args__ = {
        'polymorphic_identity':'employee'
    }

    def __init__(self, first_name, last_name, address, type, manager_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.type = type
        self.manager_id = manager_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'address' : self.address,
            'type' : self.type,
            'manager_id' : self.manager_id
        }

'''
Helper functions

'''
def get_vehicle(id):
    if id <= 0:
        return Vehicle.query.all()
    else:
        return Vehicle.query.filter_by(id=id).first()

def get_customer(id):
    if not id:
        return Customer.query.all()
    else:
        return Customer.query.filter_by(id=id).first()

def get_employee(id):
    if not id:
        return Employee.query.all()
    else:
        return Employee.query.filter_by(id=id).first()

def get_manager(id):
    if not id:
        return Manager.query.all()
    else:
        return Manager.query.filter_by(id=id).first()

def get_reservation():
    return Reservation.query.all()