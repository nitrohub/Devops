import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Import the Flask app

class FlaskRouteTest(unittest.TestCase):
    def test_invalid_method(self):
        # Use Flask's test client to simulate a POST request to the home route
        with app.test_client() as client:
            response = client.post('/')  # Home route accepts only GET
            self.assertEqual(response.status_code, 405)  # Expect 405 Method Not Allowed

if __name__ == '__main__':
    unittest.main()
