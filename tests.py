import unittest
from fastapi.testclient import TestClient

# Import your FastAPI app from main.py
from app import app

# Remember to change the id in the url to an id that isn't in the database otherwise you will get an error
class TestFastAPIApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_home_endpoint(self):
        response = self.client.get('/api/1')
        self.assertEqual(response.status_code, 200)

    def test_addPerson_endpoint(self):
        json_data = {
            "name": "John Doe",
            "age": 30,
            "track": "backend"
        }
    
        response = self.client.post('api/', json=json_data)
        self.assertEqual(response.status_code, 200)

    def test_edit_endpoint(self):
        json_data = {
            "name": "Mill",
            "age": 22,
            "track": "frontend"
        }

        response = self.client.patch('api/1', json=json_data)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_endpoint(self):
        response = self.client.delete('api/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()