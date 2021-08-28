import os
import enum
from typing import Counter
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint, Table, MetaData
from sqlalchemy.sql.sqltypes import Boolean, Float
from config import init_env_vars
Base = declarative_base()


init_env_vars()
database_name = "car_rental"
database_username = os.getenv('DB_USER') 
database_password = os.getenv('DB_PASSWORD')
database_path = "postgresql://{}:{}@{}/{}"\
  .format(database_username, database_password, 'localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    Migrate(app, db)

def session_revert():
  db.session.rollback()

def session_close():
  db.session.close()

'''
Schema Configuration

'''
class Reservation (db.Model):
    __tablename__ = 'reservation'
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'),   primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    # implementing time always sucks, will come back if enough time
    # start_time = 
    # end_time = 
    cost = Column(Float, nullable=False)
    vehicle  = relationship('Vehicle', uselist=False, foreign_keys=[vehicle_id])
    customer = relationship('Customer', uselist=False, foreign_keys=[customer_id])
    employee = relationship('Employee', uselist=False, foreign_keys=[employee_id])

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
    currently_renting = Column(Boolean, nullable=False)
    reservations = relationship('Reservation', back_populates='customer')

    __mapper_args__ = {
        'polymorphic_identity':'customer'
    }

    def __init__(self, first_name, last_name, address, type, currently_renting):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.type = type
        self.currently_renting = currently_renting

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
            'currently_renting' : self.currently_renting
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