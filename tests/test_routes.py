import unittest
from app import app

class FlaskRouteTest(unittest.TestCase):
    
    def test_invalid_method(self):
        # Use Flask's test client to simulate a POST request to the /home route
        with app.test_client() as client:
            response = client.post('/')  # Home route accepts only GET
            self.assertEqual(response.status_code, 405)  # Expect 405 Method Not Allowed

if __name__ == '__main__':
    unittest.main()