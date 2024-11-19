import unittest
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus  # Add this import for URL encoding

# Load environment variables from .env file
load_dotenv()

class MongoDBConnectionTest(unittest.TestCase):

    def setUp(self):
        """Setup for MongoDB connection"""
        # Fetch MongoDB credentials from environment variables
        self.MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
        self.MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

        # URL-encode the username and password
        self.encoded_username = quote_plus(self.MONGODB_USERNAME)
        self.encoded_password = quote_plus(self.MONGODB_PASSWORD)

        # Connect to MongoDB and assign the client to self.client
        self.client = MongoClient(f"mongodb+srv://myuser:{self.encoded_password}@cluster0.tf8t0.mongodb.net/shop_db?retryWrites=true&w=majority&tls=true")

    def test_mongo_connection(self):
        """Test MongoDB connection by pinging the server"""
        try:
            # Ping the MongoDB server to check the connectivity
            self.client.admin.command('ping')
            print("MongoDB connection successful.")
            connected = True
        except ServerSelectionTimeoutError:
            connected = False
        except ConnectionFailure:
            connected = False
        
        self.assertTrue(connected)  # Assert that MongoDB is connected

    def tearDown(self):
        """Teardown MongoDB connection"""
        # Ensure client exists and close it
        if hasattr(self, 'client'):
            self.client.close()

if __name__ == '__main__':
    unittest.main()
