import sqlite3
import os
import unittest
from fastapi.testclient import TestClient
from main import app


cleanup = True

def setup_database():
    #remove excisting test database if there is one
    teardown_database()
    
    # create database file
    test_db = open("test_database.db", "w")
    test_db.close()

    # connect to test database
    con = sqlite3.connect("test_database.db")
    cur = con.cursor()

    # run sql schema from file
    with open("schema.sql", "r") as f:
        schema = f.read()

    # populate database
    with open("populate.sql") as f:
        populate = f.read()

    cur.executescript(schema)
    cur.executescript(populate)
    con.commit()
    con.close()

def teardown_database():
    if os.path.exists("test_database.db") & cleanup:
        os.remove("test_database.db")

class GetAllDatasets(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)


    def test_backend_returns_list_of_dataset(self):
        response = self.client.get(
            "/datasets/"
        )
        
        self.assertIsNotNone(response.text)
        assert response.status_code == 200


    @classmethod  
    def teardown_class(self):
        teardown_database()


class AddNewDataset(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)


    def test_adding_new_dataset(self):
        response = self.client.post(
            "/datasets/?dataset_name=test&dataset_desc=this%20is%20a%20test%20dataset"
        )
        
        assert response.status_code == 201

        check_added = self.client.get(
            "/datasets/"
        )
        self.assertIn("test", check_added.text) 
        


    @classmethod  
    def teardown_class(self):
        teardown_database()


if __name__ == '__main__':
    unittest.main()
