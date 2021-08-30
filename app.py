import sqlalchemy
from auth import *
import os
from flask import Flask, request, abort, jsonify, Response
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

  @app.route('/')
  def index():
    abort(400)

  @app.route('/vehicles',  methods=['GET'])
  def vehicles():
    try:
      vehicles = get_vehicle(0)
      return jsonify({
        "success" : 200,
        "message" : "OK",
        "vehicles" : [vehicle.format() for vehicle in vehicles]
      })
    except Exception:
        abort(404)
    finally:
      session_close()

  @app.route('/vehicles/<int:id>', methods=['GET'])
  def certain_vehicle(id):
      try:
        vehicle = get_vehicle(id)
        return jsonify({
          "success" : 200,
          "message" : "OK",
          "vehicle" : vehicle.format()
      })
      except Exception:
        abort(404)
      finally:
        session_close()

  
  @app.route('/vehicles', methods=['POST'])
  @requires_auth('add:vehicle')
  def add_vehicle(jwt):
    data = request.get_json()
    try:
    # All new cehicles default "False" for last Vehicle param attribute
    # "currently_rented"
      new_vehicle = Vehicle(data['make'],
                            data['model'],
                            data['year'],
                            data['body_style'],
                            data['color'],
                            False)
      Vehicle.insert(new_vehicle)
      return jsonify({
        "success" : 201,
        "message" : "Vehicle added",
      }), 201
    except Exception:
      session_revert()
      abort(422)
    finally:
      session_close()

  @app.route('/vehicles/<int:id>', methods=['PATCH'])
  @requires_auth('update:vehicle')
  def update_vehicle(jwt, id):
    data = request.get_json()
    try:
        target_vehicle = Vehicle.query.filter(Vehicle.id==id).first()
        # if vehicle id is not found, abort 404
        if target_vehicle is None:
          abort(404)
        if "make" in data:
            target_vehicle.make = data['make']
        if "model" in data:
            target_vehicle.model = data['model']
        if "year" in data:
            target_vehicle.year = data['year']
        if "body_style" in data:
            target_vehicle.body_style = data['body_style']
        if "color" in data:
            target_vehicle.color = data['color']
        # update the currently_rented field to see if there is any 
        # open reservation with the vehicle being updated
        reservation = db.session.query(Reservation).join(Vehicle).first()
        if reservation is None:
          target_vehicle.currently_rented = False
        else:
          target_vehicle.currently_rented = True
        Vehicle.update(target_vehicle)
        updated_vehicle =\
           Vehicle.query.filter(Vehicle.id == target_vehicle.id).first()
        return jsonify({
            "success" : 200,
            "message" : "Vehicle updated",
            "updated_vehicle" : [updated_vehicle.format()]
        })
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        session_revert()
        abort(404)
    except TypeError:
        session_revert()
        abort(404)
    except AttributeError:
        session_revert()
        abort(404)
    finally:
        session_close()

  @app.route('/vehicles/<int:id>', methods=['DELETE'])
  @requires_auth('delete:vehicle')
  def remove_vehicle(jwt, id):
    try:
        target_vehicle = Vehicle.query.filter(Vehicle.id==id).first()
        # if vehicle is currently being rented, it cannot be deleted. Abort 422.
        if target_vehicle.currently_rented:
          abort(422)
        Vehicle.delete(target_vehicle)
        return jsonify({
            "success" : 200,
            "message" : "Vehicle deleted",
        })
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        session_revert()
        abort(404)
    except TypeError:
        session_revert()
        abort(404)
    except AttributeError:
        session_revert()
        abort(404)
    finally:
        session_close()

  @app.route('/customers', methods=['GET'])
  @requires_auth('get:customer')
  def customers(jwt):
    try:
      customers = get_customer(0)
      return jsonify({
          "success" : 200,
          "message" : "OK",
          "customers" : [customer.format() for customer in customers]
      })
    except Exception:
        abort(404)
    finally:
      session_close()
  
  @app.route('/customers', methods=['POST'])
  @requires_auth('add:customer')
  def add_customers(jwt):
    data = request.get_json()
    try:
      new_cust = Customer(data['first_name'],
                            data['last_name'],
                            data['address'],
                            "customer")
      Customer.insert(new_cust)
      return jsonify({
        "success" : 201,
        "message" : "Customer added" 
      }), 201
    except Exception:
        session_revert()
        abort(422)
    finally:
      session_close()


  @app.route('/managers', methods=['GET'])
  @requires_auth('get:manager')
  def managers(jwt):
    try:
      managers = get_manager(0)
      return jsonify({
          "success" : 200,
          "message" : "OK",
          "managers" : [manager.format() for manager in managers]
      })
    except Exception:
        abort(404)
    finally:
      session_close()
  
  @app.route('/managers', methods=['POST'])
  @requires_auth('add:manager')
  def add_managers(jwt):
    data = request.get_json()
    try:
      new_manager = Manager(data['first_name'],
                            data['last_name'],
                            data['address'],
                            "manager")
      Manager.insert(new_manager)
      return jsonify({
        "success" : 201,
        "message" : "Manager added" 
      }), 201
    except Exception:
      session_revert()
      abort(422)
    finally:
      session_close()


  @app.route('/employees', methods=['GET'])
  @requires_auth('get:employee')
  def employees(jwt):
    try:
      employees = get_employee(0)
      return jsonify({
          "success" : 200,
          "message" : "OK",
          "employees" : [employee.format() for employee in employees]
      })
    except Exception:
        abort(404)
    finally:
      session_close()
  
  @app.route('/employees', methods=['POST'])
  @requires_auth('add:employee')
  def add_employees(jwt):
    data = request.get_json()
    try:
      new_emp = Employee(data['first_name'],
                            data['last_name'],
                            data['address'],
                            "employee",
                            data['manager_id'])
      Employee.insert(new_emp)
      return jsonify({
        "success" : 201,
        "message" : "Employee added" 
      }), 201
    except Exception:
      session_revert()
      abort(422)
    finally:
      session_close()

  @app.route('/reservations', methods=['GET'])
  @requires_auth('get:reservation')
  def reservations(jwt):
    try:
      reservations = get_reservation()
      return jsonify({
        "success" : 200,
        "message" : "OK",
        "reservations" : [reservation.format() for reservation in reservations]
      })
    except Exception:
      abort(404)
    finally:
      session_close()
  
  @app.route('/reservations', methods=['POST'])
  @requires_auth('add:reservation')
  def add_reservations(jwt):
    data = request.get_json()
    try:
      target_vehicle = \
        Vehicle.query.filter(Vehicle.id==data['vehicle_id']).first()
      if target_vehicle is None:
        abort(404)
      # A reservation can not be opened with a car already being rented,
      # Therefore will cause an abort 422
      if target_vehicle.currently_rented:
        abort(422)
      # All new reservations default "True" for last Reservation param attribute
      # "reservation_open"
      new_res = Reservation(data['vehicle_id'],
                            data['customer_id'],
                            data['employee_id'],
                            data['cost'],
                            True)  
      Reservation.insert(new_res)
      return jsonify({
        "success" : 201,
        "message" : "Reservation added" 
      }), 201
    except sqlalchemy.exc.IntegrityError:
      session_revert()
      abort(422)
    finally:
      session_close()

  @app.route('/reservations/<int:id>', methods=['PATCH'])
  @requires_auth('update:reservation')
  def update_reservation(jwt, id):
    data = request.get_json()
    try:
      target_reservation = Reservation.query.filter(Reservation.id==id).first()
      if target_reservation is None:
        abort(404)
      if "cost" in data:
          target_reservation.cost = data['cost']
      if "vehicle_id" in data:
        # Cannot update a reservation using a vehicle that is already rented 
        # out, will abort for 422
        target_vehicle = Vehicle.query.filter(id=data['vehicle_id']).first()
        if target_vehicle.currently_rented:
          abort(422)
        else:
          target_reservation.vehicle_id = data['vehicle_id']
          Vehicle.update(target_vehicle)
      if "reservation_open" in data:
        target_reservation.reservation_open = data['reservation_open']
      if "customer_id" in data:
          target_reservation.customer_id = data['customer_id']
      if "employee_id" in data:
          target_reservation.employee_id = data['employee_id']
      updated_reservation = Reservation.query.filter(Reservation.id==id).first()
      return jsonify({
          "success" : 200,
          "message" : "Reservation updated",
          "updated_vehicle" : [updated_reservation.format()]
      })
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        session_revert()
        abort(404)
    except TypeError:
        session_revert()
        abort(404)
    except AttributeError:
        session_revert()
        abort(404)
    finally:
        session_close()

  
  @app.errorhandler(AuthError)
  def AuthErrorHandler(error):
    return jsonify({
        "error": error.description,
        "message": error.code['code']
    }), error.description

  @app.errorhandler(400)
  def unprocessable(error):
      return jsonify({
          "error": 400,
          "message": "Bad request"
      }), 400
    
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "error": 422,
          "message": "Unprocessable request"
      }), 422

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "error": 404,
          "message": "Resource not found"
      }), 404

  @app.errorhandler(401)
  def unauthorized(error):
      return jsonify({
          "error": 401,
          "message": "Unauthorized"
      }), 401

  @app.errorhandler(403)
  def forbidden(error):
      return jsonify({
          "error": 403,
          "message": "Forbidden"
      }), 403
    
  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)