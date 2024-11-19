import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app import db

class MongoDBWriteTest(unittest.TestCase):
    
    def test_insert_product(self):
        # Create a test product document
        product = {
            "name": "Test Product",
            "price": 19.99,
            "category": "Test Category"
        }
        
        # Insert the document into MongoDB
        result = db.products.insert_one(product)
        
        # Query the database to find the inserted document
        inserted_product = db.products.find_one({"name": "Test Product"})
        
        # Verify that the product was successfully inserted
        self.assertIsNotNone(inserted_product)
        self.assertEqual(inserted_product['name'], "Test Product")
        self.assertEqual(inserted_product['price'], 19.99)
        
        # Cleanup: Remove the inserted product after the test
        db.products.delete_one({"name": "Test Product"})

if __name__ == '__main__':
    unittest.main()
