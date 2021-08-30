import os

def init_env_vars():
    os.environ['DB_USER'] = 'postgres'
    os.environ['DB_PASSWORD'] = 'marshall'
    os.environ['TEST_DB_NAME'] = 'car_rental_test'
    os.environ['DB_NAME'] = 'car_rental'
    os.environ['MANAGER_TOKEN'] = 'Bearer ' + '<token>'
