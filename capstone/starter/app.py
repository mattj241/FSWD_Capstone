import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Vehicle, setup_db, session_revert, session_close

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

  @app.route('/vehicles', methods=['GET'])
  def get_vehicles():
    vehicles = Vehicle.query.all()
    dict = {}
    for vehicle in vehicles:
      dict.update(vehicle.format())
    return dict
  
  @app.route('/vehicles', methods=['POST'])
  def add_vehicle():
    data = request.get_json()
    # try:
    new_vehicle = Vehicle(data['make'],
                          data['model'],
                          data['year'],
                          data['body_style'],
                          data['color'],
                          data['currently_rented'],
                          data['renter_id'],
                          data['home_branch_id'])
    Vehicle.insert(new_vehicle)
    # except Exception:
    #   session_revert()
    #   abort(422)
    # finally:
    #   session_close()
    return jsonify({
        "message" : "201 Question successfully created" 
      })
    
  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)