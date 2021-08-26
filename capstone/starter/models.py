import os
import enum
from typing import Counter
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from config import init_env_vars

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

Base = declarative_base()

class Vehicle(db.Model):
    __tablename__= 'vehicle'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    body_style = Column(String)
    color = Column(String)
    currently_rented = Column(Boolean, nullable=False)
    renter_id = relationship('Customer', backref='vehicles', uselist=False)
    home_branch_id = relationship('Branch', backref='vehicles', uselist=False)

    def __init__(self, make, model, year, body_style, color,
                currently_rented, renter_id, home_branch_id):
        self.make = make
        self.model = model
        self.year = year
        self.body_style = body_style
        self.color = color
        self.currently_rented = currently_rented
        self.renter_id = renter_id
        self.home_branch_id = home_branch_id

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
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'body_style': self.body_style,
            'color': self.color,
            'currently_rented': self.currently_rented,
            'renter_id': self.renter_id,
            'home_branch_id': self.home_branch_id
        }

class Person(db.Model):
    __abstract__ = True

    first_name = Column(String, nullable=False)
    last_name  = Column(String, nullable=False)
    address = Column(String, nullable=False)
    currently_renting = Column(Boolean, nullable=False)

    # Credit: https://learnings.desipenguin.com/post/fk_abstract_class_sqlalchemy/
    @declared_attr
    def vehicle_id(cls):
        rented_vehicle = Column(Integer, ForeignKey('vehicle.id'))

    def __init__(self, first_name, last_name, address, currently_renting, body_style, color,
                rented_vehicle):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.currently_renting = currently_renting
        self.rented_vehicle = rented_vehicle

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
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'address' : self.address,
            'currently_renting' : self.currently_renting,
            'rented_vehicle' : self.rented_vehicle,
        }

class Branch(db.Model):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    # staff = relationship('Staff', backref='branch')
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

    def __init__(self, name, address, staff):
        self.name = name
        self.address = address
        self.staff = staff

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
            'name' : self.name,
            'address' : self.address,
            'staff' : self.staff
        }
class Customer(Person):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))


class Staff(Person):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    branch = Column(Integer, ForeignKey('branch.id'))