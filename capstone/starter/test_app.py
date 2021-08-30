import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import *

MANAGER_TOKEN = os.getenv('MANAGER_TOKEN')


class TriviaTestCase(unittest.TestCase):
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

    def test_vehicles(self):
        res = self.client().get('/vehicles')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()