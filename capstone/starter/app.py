import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import *

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)

  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', \
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', \
                         'GET,PATCH,POST,DELETE')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

  @app.route('/vehicles/',  methods=['GET'])
  def get_vehicles():
    vehicles = Vehicle.query.all()
    dict = {}
    for vehicle in vehicles:
      dict.update(vehicle.format())
    return dict

  @app.route('/vehicles/<int:id>', methods=['GET'])
  def get_vehicle(id):
      vehicle = Vehicle.query.filter_by(id=id).first()

      return vehicle.format()
  
  @app.route('/vehicles', methods=['POST'])
  def add_vehicle():
    data = request.get_json()
    try:
      new_vehicle = Vehicle(data['make'],
                            data['model'],
                            data['year'],
                            data['body_style'],
                            data['color'],
                            data['currently_rented'])
      Vehicle.insert(new_vehicle)
    except Exception:
      session_revert()
      abort(422)
    finally:
      session_close()
    return jsonify({
        "message" : "201 Vehicle added" 
      })

  @app.route('/customers', methods=['GET'])
  def get_customers():
    customers = Customer.query.all()
    dict = {}
    for customer in customers:
      dict.update(customer.format())
    return dict
  
  @app.route('/customers', methods=['POST'])
  def add_customers():
    data = request.get_json()
    # try:
    new_cust = Customer(data['first_name'],
                          data['last_name'],
                          data['address'],
                          data['type'],
                          data['currently_renting'])
    Customer.insert(new_cust)
    # except Exception:
    #   session_revert()
    #   abort(422)
    # finally:
    #   session_close()
    return jsonify({
        "message" : "201 Customer added" 
      })

  @app.route('/managers', methods=['GET'])
  def get_managers():
    managers = Manager.query.all()
    dict = {}
    for manager in managers:
      dict.update(manager.format())
    return dict
  
  @app.route('/managers', methods=['POST'])
  def add_managers():
    data = request.get_json()
    # try:
    new_manager = Manager(data['first_name'],
                          data['last_name'],
                          data['address'],
                          data['type'])
    Manager.insert(new_manager)
    # except Exception:
    #   session_revert()
    #   abort(422)
    # finally:
    #   session_close()
    return jsonify({
        "message" : "201 Manager added" 
      })

  @app.route('/employees', methods=['GET'])
  def get_employees():
    employees = Employee.query.all()
    dict = {}
    for employee in employees:
      dict.update(employee.format())
    return dict
  
  @app.route('/employees', methods=['POST'])
  def add_employees():
    data = request.get_json()
    try:
      new_cust = Employee(data['first_name'],
                            data['last_name'],
                            data['address'],
                            data['type'],
                            data['manager_id'])
      Employee.insert(new_cust)
    except Exception:
      session_revert()
      abort(422)
    finally:
      session_close()
    return jsonify({
        "message" : "201 Employee added" 
      })
    
  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)