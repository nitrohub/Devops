import unittest
from app import db
from pymongo.errors import ConnectionError

class MongoDBConnectionTest(unittest.TestCase):
    
    def test_mongo_connection(self):
        try:
            db.client.admin.command('ping')  # Ping MongoDB server to check connectivity
            connected = True
        except ConnectionError:
            connected = False
        
        self.assertTrue(connected)  # Assert that MongoDB is connected

if __name__ == '__main__':
    unittest.main()
